from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from products.models import Product
from products.permissions import ProductPermission
from products.serializers import ProductSerializers, ProductDetailSerializers
from rest_framework import viewsets
from django_filters import rest_framework as filters

class ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['price']


class ProductViewSet(viewsets.ModelViewSet):
    '''предоставляет для фронта информацию о продуктах'''
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    serializer_classes = {
        'retrieve': ProductDetailSerializers,
        'create': ProductDetailSerializers,
    }
    lookup_field = 'pk'
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['product']
    search_fields = ['name', 'price']
    ordering_fields = ['name', 'price']
    filterset_class = ProductFilter
    permission_classes = (ProductPermission,)

