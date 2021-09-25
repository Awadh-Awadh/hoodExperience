from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.
# user
#neighbourhood
#profile
#Business


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    def __str__(self):
        return self.username

# class profile(models.Model):
#     name = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
#     email = models.CharField(max_length=200)
#     neighbourhood = models.ForeignKey("Neighbourhood", on_delete=models.CASCADE)

# class Neighbourhood(models.Model):
#     pass