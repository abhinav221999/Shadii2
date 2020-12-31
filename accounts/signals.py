from .models import Relationship
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Relationship)
def post_save_add_to_friends(sender, instance, created, **kwargs):
    print('something')
    sender_ = instance.sender
    receiver_ = instance.receiver
    print(sender_.fname, receiver_.fname)
    if instance.status == 'accepted':
        sender_.friends.add(receiver_.user)
        receiver_.friends.add(sender_.user)
        sender_.save()
        receiver_.save()

