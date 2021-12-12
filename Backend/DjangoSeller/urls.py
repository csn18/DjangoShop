from django.contrib import admin
from django.urls import path, include
from Accounts.router import urlpatterns as url_accounts
from Shop.router import urlpatterns as url_shop


urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += url_accounts
urlpatterns += url_shop
