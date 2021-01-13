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
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
import json
from django.contrib.auth.decorators import login_required
from .decorators import *


@unauthenticated_user
def Login(request):
    if request.user.is_authenticated:
        if hasattr(request.user, 'profile'):
            return HttpResponse('login successful')
        else:
            return redirect('info')
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
        if hasattr(user, 'profile'):
            return redirect('home')
        else:
            return redirect('info')
    else:
        messages.info(request, 'Username or Password is incorrect')
        return HttpResponse('login failed')


def verification(request, uid, token):

    id = force_str(urlsafe_base64_decode(uid))
    user = User.objects.get(pk=id)
    if not token_generator.check_token(user, token):
        return HttpResponse('account already activated')

    if user.is_active:
        return redirect('login')
    user.is_active = True
    user.save()

    messages.success(request, 'Account activated successfully')
    return redirect('login')


@login_required(login_url='login')
@profile_not_exists
def info(request):
    if request.method == 'POST':
        temp = json.loads(request.body.decode('utf-8'))
        customer = Profile()
        customer.fname = temp['firstname']
        customer.lname = temp['lastname']
        customer.gender = temp['gender']
        customer.religion = temp['religion']
        customer.language = temp['language']
        customer.date = parse_date(temp['dob'])
        customer.agepref = int(temp['agepref'])
        customer.qualification = temp['qualification']
        customer.user = request.user
        customer.save()
        for interest in temp['interest_list']:
            if not Interest.objects.filter(interest=interest).exists():
                choice = Interest(interest=interest)
                choice.save()
                customer.interests.add(choice)
            else:
                choice = Interest.objects.filter(interest=interest)[0].id
                customer.interests.add(choice)
        return HttpResponseRedirect(reverse('login'))
    return render(request, 'accounts/form.html')


@login_required(login_url="login")
def home(request):
    suggestions = request.user.profile.suggestions.all()
    context = {
        'suggestions': suggestions
    }
    return render(request, 'accounts/home.html', context)
