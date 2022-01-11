from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet

from .serializers import *
from .services import *


class AllProductViewSet(ModelViewSet):
    """
    All product Api endpoint
    """
    queryset = get_all_products()
    serializer_class = ProductSerializer


class CartViewSet(ViewSet):
    """
    Product cart api endpoint
    """

    def list(self, request):
        queryset = get_product_cart_items(request)
        serializer = CartSerializer(queryset)
        return Response(serializer.data)
