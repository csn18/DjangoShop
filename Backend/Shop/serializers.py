from rest_framework import serializers
from .models import ProductPhoto, Product, ProductCart, Customer


class ProductPhotoSerializer(serializers.ModelSerializer):
    """
    Serializer for product photo
    """

    class Meta:
        model = ProductPhoto
        fields = ['image_url']


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for product
    """
    name = serializers.CharField(required=True)
    color = serializers.SlugRelatedField(read_only=True, slug_field='name_color')
    size = serializers.SlugRelatedField(read_only=True, many=True, slug_field='size')
    gender = serializers.SlugRelatedField(read_only=True, slug_field='gender')
    manufacturer = serializers.SlugRelatedField(read_only=True, slug_field='manufacturer_name')
    type = serializers.SlugRelatedField(read_only=True, slug_field='type')
    image = ProductPhotoSerializer()

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'color',
            'size',
            'gender',
            'manufacturer',
            'type',
            'count',
            'description',
            'price',
            'image'
        ]


class CustomerSerializer(serializers.ModelSerializer):
    """
    Serializer for customer
    """
    user = serializers.SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        model = Customer
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    """
    Serializer for get product cart
    """
    customer = CustomerSerializer(read_only=True)

    class Meta:
        model = ProductCart
        fields = '__all__'
