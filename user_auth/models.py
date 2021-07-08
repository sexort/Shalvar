from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delte=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    join_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
