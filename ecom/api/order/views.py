from django.contrib.auth.backends import UserModel
from rest_framework import viewsets
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from .serializers import OrderSerializer
from .models import Order
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def validate_user_session(id, token):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk=id)
        if user.session_token == token:
            return True
        return False
    except UserModel.DoesNotExist:
        return False


@csrf_exempt
def add(request, id, token):
    # if not validate_user_session(id, token):
    #    return JsonResponse({'error': 'Please re-login', 'code': '1'})

    if request.method == 'POST':
        transaction_id = request.POST['transaction_id']
        amount = request.POST['amount']
        products = request.POST['products']
        total_pro = request.POST['total_pro']
        user = id
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        phoneNumber = request.POST['phoneNumber']
        email = request.POST['email']
        streetAddress = request.POST['streetAddress']
        postalCode = request.POST['postalCode']
        province = request.POST['province']
        city = request.POST['province']

        ordr = Order(user=user, product_names=products, total_products=total_pro, transaction_id=transaction_id, total_amount=amount, firstName=firstName,
                     lastName=lastName, phoneNumber=phoneNumber, email=email, streetAddress=streetAddress, postalCode=postalCode, province=province, city=city)
        ordr.save()
        return JsonResponse({'success': True, 'error': False, 'msg': 'Order Placed Successfully', 'id': ordr.id})


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('id')
    serializer_class = OrderSerializer
