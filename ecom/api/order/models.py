from django.db import models
from api.user.models import CustomUser
from api.product.models import Product
# Create your models here.


class Order(models.Model):
    #user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    user = models.CharField(max_length=10, null=True)
    product_names = models.CharField(max_length=500)
    total_products = models.CharField(max_length=500, default=0)
    transaction_id = models.CharField(max_length=150, default=0)
    total_amount = models.CharField(max_length=50, default=0)
    firstName = models.CharField(max_length=250, null=True)
    lastName = models.CharField(max_length=250, null=True)
    phoneNumber = models.CharField(max_length=10, null=True)
    email = models.CharField(max_length=50, null=True)
    streetAddress = models.CharField(max_length=250, null=True)
    postalCode = models.CharField(max_length=6, null=True)
    province = models.CharField(max_length=20, null=True)
    city = models.CharField(max_length=250, null=True)
    country = models.CharField(max_length=100, default="Canada")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
