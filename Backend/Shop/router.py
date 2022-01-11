from rest_framework.routers import DefaultRouter
from django.urls import path, include

from Shop.api import *

router = DefaultRouter()
router.register(r'products', AllProductViewSet)
router.register(r'cart', CartViewSet, basename='cart')

urlpatterns = [
    path('api/', include(router.urls)),
]
