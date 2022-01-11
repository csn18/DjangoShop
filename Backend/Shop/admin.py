from django.contrib import admin
from .models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'color', 'count']
    list_editable = ['price', 'color', 'count']


@admin.register(ProductCart)
class ProductCartAdmin(admin.ModelAdmin):
    list_display = ['product', 'customer']


admin.site.register(ProductColor)
admin.site.register(ProductType)
admin.site.register(ProductSize)
admin.site.register(Manufacturer)
admin.site.register(GenderType)
admin.site.register(Customer)
admin.site.register(ProductPhoto)
