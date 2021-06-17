from django.db import models
from api.category.models import Category
from api.brands.models import Brands

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.CharField(max_length=50)
    stock = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True, blank=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    age_target = models.CharField(max_length=3, default=0)
    max_Order_qty = models.CharField(max_length=2, default=5)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True)
    brands = models.ForeignKey(
        Brands, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
