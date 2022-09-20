from products.models import Category, Product
from rest_framework import serializers


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