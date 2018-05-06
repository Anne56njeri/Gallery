from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length = 60)
    @classmethod
    def search(cls,search_term):
        categories=cls.objects.filter(name__icontains=search_term)
        return categories
    
class Image(models.Model):
    name=models.CharField(max_length=30)
    image_description=models.TextField()
    image_path=models.ImageField(upload_to='images/',blank=True)
    category=models.ForeignKey(Category,null=True)
