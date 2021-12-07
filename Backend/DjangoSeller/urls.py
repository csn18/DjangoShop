from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Shop.api import *

router = DefaultRouter()
router.register(r'products', AllProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
