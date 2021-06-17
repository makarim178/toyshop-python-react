from rest_framework import serializers
from .models import Brands


class BrandsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brands
        fields = ('id', 'name')
