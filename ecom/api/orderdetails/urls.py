from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'', views.OrderdetailsViewSet)

urlpatterns = [
    path('add/', views.add, name="orderdetails.add"),
    path('', include(router.urls))
]
