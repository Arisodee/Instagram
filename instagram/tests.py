from django.test import TestCase
from.models import Profile, Post

# Create your tests here.

class ProfileTestClass(TestCase):

    def setUp(self):
        self.Ariso = Profile(name = 'Ariso', profile_pic = 'image.jpg', bio='Baking your world a better place one cake at a time.')
        self.Ariso.save()

    def tearDown(self):
        Profile.objects.all().delete()
    

    def test_instance(self):
        self.assertTrue(isinstance(self.Ariso, Profile))

    def test_save_method(self):
        self.Ariso.save_profile()
        name = Profile.objects.all()

    def test_delete_method(self):
        self.profile_pic.delete_profile_pic()
        Profile = Profile.objects.all()
        self.assertTrue(len(Locations)==2) 



class PostTestCase(TestCase):

    def setUp(self):
        self.baking = Profile(image= 'image.jpg', title = 'baking', user='User')
        self.baking.save()


    def tearDown(self):
        Post.objects.all().delete()


    def test_instance(self):
        self.assertTrue(isinstance(self.baking, Post))


    def  test_save_method(self):
        self.Ariso.save_post()
        tittle = Post.objects.all()
