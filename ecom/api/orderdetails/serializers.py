from django.db.models import fields
from rest_framework import serializers
from .models import Orderdetails


class OrderDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Orderdetails
        fields = ('orderid', 'productid', 'productname',
                  'productqty', 'productprice')
