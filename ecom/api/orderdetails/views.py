from rest_framework import viewsets
from .serializers import OrderDetailsSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Orderdetails

# Create your views here.


@csrf_exempt
def add(request):
    if request.method == 'POST':
        orderid = request.POST['orderid']
        productid = request.POST['productid']
        productname = request.POST['productname']
        productqty = request.POST['productqty']
        productprice = request.POST['productprice']
        ordrdtls = Orderdetails(orderid=orderid, productid=productid,
                                productname=productname, productqty=productqty, productprice=productprice)
        ordrdtls.save()
        return JsonResponse({'success': True, 'error': False, 'msg': 'Order Placed Successfully'})


class OrderdetailsViewSet(viewsets.ModelViewSet):
    queryset = Orderdetails.objects.all().order_by('id')
    serializer_class = OrderDetailsSerializer
