from django.db.models import Count, F
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from products.models import Product, ProductComment, ProductLike, ProductRating
from products.permissions import ProductPermission
from products.serializers import ProductSerializers, ProductDetailSerializers, ProductCommentSerializers, \
    RatingSerializers
from rest_framework import viewsets, status
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
    # для просмотра комментариев в деталях продукта
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


    # для просмотра комментариев в деталях продукта
    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)

    def get_queryset(self):
        queryset = Product.objects.annotate(
            category_name=F('category__name'),
            owner_name=F('user__username'),
            likes_count=Count('likes'),
        ).order_by('-id')
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# настройка комментариев
class CommentView(ModelViewSet):
    queryset = ProductComment.objects.all()
    serializer_class = ProductCommentSerializers
    lookup_field = 'pk'

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(
            user=self.request.user,
            product_id=kwargs.get('product_pk')
        )
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


# настройка лайков
class ProductLikeView(APIView):

    def get(self, request, product_pk):
        created = ProductLike.objects.filter(product_id=product_pk, user=request.user).exists()
        if created:
            ProductLike.objects.filter(
                product_id=product_pk,
                user=request.user
            ).delete()
            return Response({'success': 'unliked'})
        else:
            ProductLike.objects.create(product_id=product_pk, user=request.user)
            return Response({'success': 'liked'})


# настройка рейтинга
class RatingView(ModelViewSet):
    queryset = ProductRating.objects.all()
    serializer_class = RatingSerializers

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(
            user=self.request.user,
            product_id=kwargs.get('product_pk')
        )
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)