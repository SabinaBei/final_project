from products.models import Category, Product, ProductComment
from rest_framework import serializers


# настройка комментариев
class ProductCommentSerializers(serializers.ModelSerializer):

    class Meta:
        model = ProductComment
        fields = '__all__'
        extra_kwargs = {
            'user': {'read_only': True},
            'product': {'read_only': True}
        }


# для просмотра комментариев в деталях продукта
class ProductDetailSerializers(serializers.ModelSerializer):
    category_name = serializers.CharField(read_only=True)
    owner_name = serializers.CharField(read_only=True)
    comments = ProductCommentSerializers(many=True)
    likes_count = serializers.IntegerField()


    class Meta:
        model = Product
        fields = (
            'id', 'name', 'price', 'description', 'category', 'user',
            'category_name', 'owner_name', 'comments', 'likes_count'
        )
        extra_kwargs = {'user': {'read_only': True}}


class ProductSerializers(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['name', 'price', 'category', 'available']
        extra_kwargs = {'user': {'read_only': True}}


class CategorySerializers(serializers.ModelSerializer):
    product_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = '__all__'

