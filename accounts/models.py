from django.db import models
from django.contrib.auth.models import User


class Interest(models.Model):
    interest = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.interest


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=50, null=True)
    lname = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=50, null=True)
    religion = models.CharField(max_length=50, null=True)
    language = models.CharField(max_length=50, null=True)
    date = models.DateField(max_length=8, null=True)
    agepref = models.IntegerField(null=True)
    qualification = models.CharField(max_length=50, null=True)
    interests = models.ManyToManyField(Interest, blank=True)
    friends = models.ManyToManyField(User, related_name='friends', blank=True)
    suggestions = models.ManyToManyField("self", related_name='suggestions', blank=True)
    avatar = models.ImageField(default='static/avatar.png', upload_to='avatars/', blank=True)

    def __str__(self):
        return self.fname


Status_choices = (
    ('sent', 'sent'),
    ('accepted', 'accepted'),
)


class Relationship(models.Model):
    sender = models.ForeignKey(Profile, related_name='sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(Profile, related_name='receiver', on_delete=models.CASCADE)
    status = models.CharField(max_length=8, choices=Status_choices)
