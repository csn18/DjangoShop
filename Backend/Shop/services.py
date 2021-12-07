from .models import *


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


def get_customer_product_cart(customer_id):
    """
    Get customer from database
    """
    customer = Customer.objects.get(id=customer_id)
    return ProductCart.objects.filter(customer=customer)
