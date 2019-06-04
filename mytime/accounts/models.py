from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="profile_images", default="default_avatar/default.png")

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)


