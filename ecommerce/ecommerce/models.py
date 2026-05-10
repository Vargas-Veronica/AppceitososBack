from django.db import models
from django.conf import settings


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)  
    description = models.TextField(blank=True, null=True)  
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    stock = models.IntegerField()  
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)  
    image = models.ImageField(upload_to='products/', blank=True, null=True)  
    is_active = models.BooleanField(default=True)  
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return self.name
    
    def get_image_url(self):
        if self.image:
            return f"{settings.MEDIA_URL}{self.image.name}"  # Solo devuelve la URL correcta
        return None

class Category(models.Model):
    name = models.CharField(max_length=255)  
    description = models.TextField(blank=True, null=True)  
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.name
