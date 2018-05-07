from django.test import TestCase
from .models import Category,Location,Image

# Create your tests here.
class CategoryTestClass(TestCase):
    def setUp(self):
        self.one=Category(name='Travel')
        self.two=Category(name='Destination')
    def test_instance(self):
        self.assertTrue(isinstance(self.one,Category))
    def test_save(self):
        self.one.save_category()
        cat=Category.objects.all()
        self.assertTrue(len(cat)>0)
    def test_delete(self):
        self.two.save_category()
        self.one.delete_category()
        cats=Category.objects.all()
        self.assertTrue(len(cats)>0)
class LocationTestClass(TestCase):
    def setUp(self):
        self.first=Location(location_name='London')
    def test_instance_2(self):
        self.assertTrue(isinstance(self.first,Location))
