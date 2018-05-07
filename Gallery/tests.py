from django.test import TestCase
from .models import Category,Location,Images

# Create your tests here.
class CategoryTestClass(TestCase):
    def setUp(self):
        self.one=Category(name='Travel')
    def test_instance(self):
        self.assertTrue(isinstance(self.one,Category))
