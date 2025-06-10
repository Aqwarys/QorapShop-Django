from rest_framework.serializers import ModelSerializer
from shop.models import Category, Product


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'sub_category', 'is_sub', 'slug']



class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'