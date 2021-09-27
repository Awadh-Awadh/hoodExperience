from django.test import TestCase
from .models import Neighbourhood,Profile,Business,Posts,CustomUser

# Create your tests here.
class TestApp(TestCase):

    #create instance

    def setUp(self) :
      self.awadh = CustomUser(email = 'awadh@gmail.com', first_name = 'awadh', last_name = 'awadh')
      self.hood = Neighbourhood(name = 'gach',location = 'juja',description = 'nice',residents = 2, admin = self.awadh,police = 2)
      self.profile = Profile(user= self.awadh, email="a@gmail.com",bio = 'awadh',hood = self.hood,pp='img.jpg')
      self.bs = Business(name = 'hired',bist_image = 'image.jpg',mobile = 254,hood = self.hood, personel = self.profile)
      self.post = Posts(image = 'post.jpg',title = 'post',caption = 'image',posted_by = self.awadh,hood = self.hood)


    def tearDown(self):
        CustomUser.objects.all().delete()
        Neighbourhood.objects.all().delete()
        Profile.objects.all().delete()
        Business.objects.all().delete()
        Posts.objects.all().delete()

   #test instances


    def test_user_instance(self):
        self.assertTrue(isinstance(self.awadh,CustomUser))

    def test_hood_instance(self):
        self.assertTrue(isinstance(self.hood,Neighbourhood))

    def test_profile_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_bs_instance(self):
        self.assertTrue(isinstance(self.bs,Business))

    def test_posts_instance(self):
        self.assertTrue(isinstance(self.post,Posts))


    #test methods