from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length = 60)
    def save_category(self):
        self.save()
    def delete_category(self):
        self.delete()

class Location(models.Model):
    location_name=models.CharField(max_length=30)
    def save_location(self):
        self.save()

class Image(models.Model):
    name=models.CharField(max_length=30)
    image_description=models.TextField()
    image_path=models.ImageField(upload_to='images/',blank=True)
    category=models.ForeignKey(Category,null=True)
    location=models.ForeignKey(Location,null=True)
    @classmethod
    def search(cls,search_term):
        categories=cls.objects.filter(category__name__icontains=search_term)
        return categories
    @classmethod
    def London(cls):
        london_images=cls.objects.filter(location__location_name='London')
        return london_images
    @classmethod
    def China(cls):
        china_images=cls.objects.filter(location__location_name='China')
        return china_images
    @classmethod
    def Malawi(cls):
        malawi_images=cls.objects.filter(location__location_name='Malawi')
        return malawi_images
    @classmethod
    def Europe(cls):
        europe_images=cls.objects.filter(location__location_name='Europe')
    def save_image(self):
        self.save()
    def delete_image(self):
        self.remove()
    @classmethod
    def get_image_by_id(cls):
        images=cls.objects.filter(id)
        return images
