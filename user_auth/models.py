from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from shalvar_installer.models import ShalvarInstallerModel


class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    join_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    @staticmethod
    @receiver(post_save, sender=ShalvarInstallerModel)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(
                user=User.objects.get(last_name=instance.website_name),
                is_verified=True,
            )
