from django.contrib.auth.models import User
from django.db import models


class ProductColor(models.Model):
    name_color = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name_color


class ProductSize(models.Model):
    size = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return f'{self.size}'


class GenderType(models.Model):
    gender = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.gender}'


class Manufacturer(models.Model):
    manufacturer_name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.manufacturer_name}'


class ProductType(models.Model):
    type = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.type}'


class ProductPhoto(models.Model):
    image_url = models.ImageField(upload_to='product/image')


class Product(models.Model):
    name = models.CharField(max_length=255)
    color = models.ForeignKey(ProductColor, on_delete=models.CASCADE, null=True)
    size = models.ForeignKey(ProductSize, on_delete=models.CASCADE, null=True)
    gender = models.ForeignKey(GenderType, on_delete=models.CASCADE, null=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, null=True)
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE, null=True)
    count = models.IntegerField(default=10)
    description = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.ForeignKey(ProductPhoto, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}'


class ProductCart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product}'
