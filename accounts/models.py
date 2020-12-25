from django.db import models
from django.contrib.auth.models import User

# Create your models here.


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
    interests = models.ManyToManyField(Interest, null=True)

    def __str__(self):
        return self.fname




