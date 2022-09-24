from products.models import Category, Product
from rest_framework import serializers

# для просмотра комментариев в деталях продукта
class ProductDetailSerializers(serializers.ModelSerializer):
    category_name = serializers.CharField(read_only=True)
    owner_name = serializers.CharField(read_only=True)


    class Meta:
        model = Product
        fields = (
            'id', 'name', 'price', 'description', 'category', 'user',
            'category_name', 'owner_name', 'likes_count', 'rating', 'comments'
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