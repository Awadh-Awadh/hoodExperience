from django.test import TestCase
from .models import Neighbourhood,Profile,Business,Posts,CustomUser

# Create your tests here.
class TestApp(TestCase):

    #test instance

    def setUp(self) :
      self.awadh = CustomUser(email = 'awadh@gmail.com', first_name = 'awadh', last_name = 'awadh')
      self.hood = Neighbourhood(name = 'gach',location = 'juja',description = 'nice',residents = 2, admin = self.awadh,police = 2,residents =2)
      self.profile = Profile(user= self.awadh, email="a@gmail.com",bio = 'awadh',hood = self.hood,pp='img.jpg')
      self.bs = Business(name = 'hired',bist_image = 'image.jpg',email = 'bs@gmail.com',mobile = 254,hood = self.hood, personel = self.profile)
      self.post = Posts(image = 'post.jpg',title = 'post',caption = 'image',posted_by = self.awadh,hood = self.hood)