#suppose we want when we delete page then user should be deleted then we need to customize it
import django.db.models.signals

from .models import Page
from django.db.models.signals import post_delete
# we need to connect signal
from django.dispatch import receiver

@receiver(post_delete, sender=Page)
def delete_related_user(sender, instance, **kwargs):
  print('page post_delete')
  instance.user.delete()

