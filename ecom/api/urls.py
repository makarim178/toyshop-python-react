from django.urls import path, include
from rest_framework.authtoken import views
from .views import home

urlpatterns = [
    path('', home, name="home"),
    path('category/', include('api.category.urls')),
    path('brands/', include('api.brands.urls')),
    path('product/', include('api.product.urls')),
    path('api-token-auth/', views.obtain_auth_token, name='api_token_auth'),
    path('user/', include('api.user.urls')),
    path('order/', include('api.order.urls')),
    path('orderdetails/', include('api.orderdetails.urls')),
    path('payment/', include('api.payment.urls')),
]
