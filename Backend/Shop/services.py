from .models import *
from rest_framework.authtoken.models import Token


def add_product(request, pk):
    """
    Add product in database
    """
    add_item = Product.objects.get(id=pk)
    customer = Customer.objects.get(id=request.user.id)
    product_cart = ProductCart(customer=customer, product=add_item)
    product_cart.save()


def get_all_products():
    """
    Get all product from database
    """
    return Product.objects.all()


def get_product_cart_items(request):
    """
    Get product form product cart
    """
    token = Token.objects.get(key=request.headers['Authorization'])
    product_cart = ProductCart.objects.get(customer=token.user)
    return product_cart
