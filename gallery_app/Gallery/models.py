from django.db import models

# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length = 60)
class Image(models.Model):
    name=models.CharField(max_length=30)
    image_description=models.TextField()
    category=models.ForeignKey(Category,null=True)
