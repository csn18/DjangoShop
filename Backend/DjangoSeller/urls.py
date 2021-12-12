from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

from Accounts.router import urlpatterns as url_accounts
from Shop.router import urlpatterns as url_shop

api_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('all-api/', api_view)
]

urlpatterns += url_accounts
urlpatterns += url_shop
