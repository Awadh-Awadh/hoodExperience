from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from cloudinary.models import CloudinaryField
from django.db.models.fields import EmailField
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
    residents = models.IntegerField(blank = True, null=True)
    admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    police = models.IntegerField(blank=True)
    health = models.IntegerField(blank=True)

    class Meta:
        ordering  = ['-pk']

    def create_neighbourhood(self):
        self.save()

    def delete_neighbourhood(self):
        self.delete()
    # @classmethod
    # def find_neighbourhood(cls, id):
    #     return cls.objects.get(id = id)
    @classmethod
    def update_hood(cls, id, update_des):
        updated_hood = cls.objects.filter(id = id).update(description = update_des)
        return updated_hood
    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email = models.CharField(max_length=200)
    bio = models.TextField()
    hood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, blank=True, null=True)
    pp = CloudinaryField('image')

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def _str__(self):
        return self.user.username



        
class Business(models.Model):
    name = models.CharField(max_length=200)
    bist_image = CloudinaryField('bist_image')
    email = models,EmailField(max_length=100, blank = True)
    mobile = models.CharField(max_length=15,blank = True)
    hood= models.ForeignKey(Neighbourhood, on_delete = models.CASCADE)
    personel = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def create_bist(self):
        self.save()

    def delete_bist(self):
        self.delete()

    @classmethod   
    def search_bist(cls, bist_name):
        return cls.objects.filter(name__icontains = bist_name).all()

    def update_bist(cls,bist_id, update_des):
        bist = cls.objects.filter(id =bist_id ).update(description = update_des )
        return bist

    def __str__(self):
       return self.name


class Posts(models.Model):
    image = CloudinaryField('post_image')
    title = models.CharField(max_length=200)
    caption = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    hood = models.ForeignKey(Neighbourhood, on_delete = models.CASCADE)
    
    def save_post(self):
        self.save()
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_posted']