from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter

from Shop.api import *

router = DefaultRouter()
router.register(r'products', AllProductViewSet)
router.register(r'products/<int:pk>/', DetailProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('Shop.urls')),
    path('api/', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


