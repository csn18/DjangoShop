from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .services import *


@login_required
def shop_page(request):
    all_items_from_shop = get_all_products()
    return render(request, 'ShopPage.html', locals())


@login_required
def add_product_to_basket(request, pk):
    add_product(request, pk)
    return redirect('shop-page')


@login_required
def get_user_cart(request):
    all_items_customer = get_customer_product_cart(request.user.id)
    return render(request, 'CartPage.html', locals())
