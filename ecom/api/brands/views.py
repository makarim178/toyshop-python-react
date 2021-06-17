from rest_framework import viewsets
from .serializers import BrandsSerializer
from .models import Brands

# Create your views here.


class BrandsViewSet(viewsets.ModelViewSet):
    queryset = Brands.objects.all().order_by('id')
    serializer_class = BrandsSerializer
