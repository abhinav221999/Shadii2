from django.db import models
from accounts.models import *


class Message(models.Model):
    author = models.ForeignKey(Profile, related_name='author_messages', on_delete=models.CASCADE)
    # author2 = models.ForeignKey(Profile, related_name='author2_messages', on_delete=models.CASCADE, null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author.fname
        #return self.author1.fname + "-->" + self.author2.fname

    def last_10_messages():
        return Message.objects.order_by('-timestamp').all()[:10]
# Create your models here.
