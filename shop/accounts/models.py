from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
def user_directory_path(instance, filename):
    return 'users/{0}/avatar/{1}'.format(instance.username, filename)


class CustomUser(AbstractUser):
    fullName = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=12, null=True, blank=True)
    src = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    alt = models.CharField(max_length=20, blank=True, null=True)
