from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from cloudinary.models import CloudinaryField
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

class Profile(models.Model):
    name = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    email = models.CharField(max_length=200)
    bio = models.TextField()
    hood = models.ForeignKey("Neighbourhood", on_delete=models.CASCADE)

locations = [
    ('juja','juja'),
    ('highpoint','highpoint'),
    ('gach','gatch'),
    ('kroad','kroad'),
    ('toll','toll')
]
class Neighbourhood(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200, choices=locations)
    description = models.TextField()
    residents = models.IntegerField(blank = True)
    admin = models.ForeignKey(Profile, on_delete=models.CASCADE)
    police = models.IntegerField(blank=True,null= True)
    health = models.IntegerField(blank=True, null = True )
    