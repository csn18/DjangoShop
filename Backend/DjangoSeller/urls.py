from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from rest_framework_swagger.views import get_swagger_view

from Accounts.router import urlpatterns as url_accounts
from Shop.router import urlpatterns as url_shop

api_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api_view)
]

urlpatterns += url_accounts
urlpatterns += url_shop
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
