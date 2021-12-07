from django.urls import path
from Backend.Shop.views import *



urlpatterns = [
    path('', shop_page, name='shop-page'),
    path('product/<int:pk>', add_product_to_basket, name='add-product-to-basket'),
    path('get_user_cart/', get_user_cart, name='get-user-cart'),
]
