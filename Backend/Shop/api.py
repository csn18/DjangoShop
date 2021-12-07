from rest_framework.viewsets import ModelViewSet

from .serializers import *
from .services import *


class AllProductViewSet(ModelViewSet):
    """
    All product Api endpoint
    """
    queryset = get_all_products()
    serializer_class = ProductSerializer
