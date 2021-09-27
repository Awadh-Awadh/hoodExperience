from cloudinary.api import update
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


    #test save methods

    def test_save_hood(self):
        self.hood.create_neighbourhood()
        n_hood = Neighbourhood.objects.all()
        self.assertTrue(len(n_hood)>0)

    def test_save_profile(self):
        self.profile.save_profile()
        user_profile = Profile.objects.all()
        self.assertTrue(len(user_profile)>0)


    def test_save_bist(self):
        self.bs.create_bist()
        bist= Profile.objects.all()
        self.assertTrue(len(bist)>0)

    def test_save_post(self):
        self.post.save_post()
        pst= Profile.objects.all()
        self.assertTrue(len(pst)>0)


    #test delete methods

    def test_delete_hood(self):
        hood = self.hood
        hood.create_neighbourhood()
        hood.delete_neighbourhood()
        user_hood = Neighbourhood.objects.all()
        self.assertEquals(len(user_hood) == 0)

    def test_delete_profile(self):
        profile = self.profile
        profile.save_profile()
        profile.delete_profile()
        user_profile = Profile.objects.all()
        self.assertEquals(len(user_profile) == 0)

    def test_delete_bist(self):
        bist = self.bs
        bist.create_bist()
        bist.delete_bist()
        user_bist = Business.objects.all()
        self.assertEquals(len(user_bist) == 0)


   #test update methods
    def test_update_hood(self):
       self.hood.create_neighbourhood()
       hood_id= Neighbourhood.objects.first().id
       Neighbourhood.update(description = 'new hood')
       new_hood = Neighbourhood.objects.get(id = hood_id)
       self.assertTrue(new_hood.description, 'new hood')


    def test_bist_update(self):
      self.bs.create_bist()
      bist_id = Business.objects.first().id
      Business.upate(description = 'New bs')
      new_bist = Business.objects.get(id = bist_id)
      self.assertTrue(new_bist.description, 'New bs' )


    def test_search_business(self):
        self.bs.create_bist()
        found = Business.search_bist('Hiring')
        self.assertTrue(len(found)==1)
