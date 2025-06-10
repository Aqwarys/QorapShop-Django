from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from .permissions import IsAdminOrReadOnly
from shop.models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly,]
    lookup_field = 'slug'
    look_value_regex = '[\w-]+'
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['is_sub',]

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly,]
    lookup_field = 'slug'
    look_value_regex = '[\w-]+'
