from rest_framework import serializers
from .models import ProductPhoto, Product


class ProductPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPhoto
        fields = ['image_url']


class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    color = serializers.SlugRelatedField(read_only=True, slug_field='name_color')
    size = serializers.SlugRelatedField(read_only=True, slug_field='size')
    image = ProductPhotoSerializer()

    class Meta:
        model = Product
        fields = [
            'name',
            'color',
            'size',
            'count',
            'price',
            'image'
        ]


class ProductDetailSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    color = serializers.SlugRelatedField(read_only=True, slug_field='name_color')
    size = serializers.SlugRelatedField(read_only=True, slug_field='size')
    gender = serializers.SlugRelatedField(read_only=True, slug_field='gender')
    manufacturer = serializers.SlugRelatedField(read_only=True, slug_field='manufacturer_name')
    type = serializers.SlugRelatedField(read_only=True, slug_field='type')
    image = ProductPhotoSerializer()

    class Meta:
        model = Product
        fields = [
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
