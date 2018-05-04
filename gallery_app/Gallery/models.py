from django.db import models

# Create your models here.
class Image(models.Model):
    name=models.CharField(max_length=30)
    image_description=models.TextField()
