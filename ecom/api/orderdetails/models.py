from django.db import models

# Create your models here.


class Orderdetails(models.Model):
    orderid = models.CharField(max_length=5)
    productid = models.CharField(max_length=5)
    productname = models.CharField(max_length=255)
    productqty = models.CharField(max_length=10)
    productprice = models.CharField(max_length=10)

    def __str__(self):
        return self.productname
