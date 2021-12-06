from rest_framework.viewsets import ModelViewSet

from .serializers import *
from .services import *


class AllProductViewSet(ModelViewSet):
    queryset = get_all_products()
    serializer_class = ProductSerializer


class DetailProductViewSet(ModelViewSet):
    queryset = get_product()
    serializer_class = ProductDetailSerializer
