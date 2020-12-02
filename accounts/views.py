from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.mail import EmailMessage
from django.urls import reverse
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from .utils import token_generator
from django.utils.dateparse import parse_date
from django.http import HttpResponse
from .models import *
import json


def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                user = User.objects.create_user(username=username, email=email)
                user.set_password(password)
                user.is_active = False
                user.save()
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                domain = get_current_site(request).domain
                link = reverse('activate', kwargs={'uid': uid, 'token': token_generator.make_token(user)})
                activate_url = 'http://'+domain+link
                email_body = 'Hi '+username+'! Please use this link to verify your account\n' + activate_url
                email = EmailMessage(
                    'Activate your account',  # subject
                    email_body,
                    'noreply@semycolon.com',  # from email address
                    [email],  # to email address
                )
                email.send(fail_silently=False)
                messages.success(request, 'Account created for ' + username)
        return redirect('login')
    return render(request, 'accounts/login.html')


def post2(request):
    username = request.POST['username2']
    password = request.POST['password2']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse('login successful')
    else:
        messages.info(request, 'Username or Password is incorrect')
        return HttpResponse('login failed')


def verification(request, uid, token):

    id = force_str(urlsafe_base64_decode(uid))
    user = User.objects.get(pk=id)
    print(user.username)

    if not token_generator.check_token(user, token):
        return HttpResponse('account already activated')

    if user.is_active:
        return redirect('login')
    user.is_active = True
    print('user activated')
    user.save()

    messages.success(request, 'Account activated successfully')
    return redirect('login')


def info(request):
    if request.method == 'POST':
        print(request.user.email)
        temp = json.loads(request.body.decode('utf-8'))
        print(temp)
        print('*******************')
        # print(dir(request))
        customer = Profile()
        customer.fname = request.POST['firstname']
        customer.lname = request.POST['lastname']
        customer.gender = request.POST['gender']
        customer.religion = request.POST['religion']
        customer.language = request.POST['language']
        customer.date = parse_date(request.POST['dob'])
        customer.agepref = int(request.POST['agepref'])
        customer.qualification = request.POST['qualification']
        customer.user = request.user
        customer.save()
        return HttpResponse('dfdssds')
    return render(request, 'accounts/form.html')


