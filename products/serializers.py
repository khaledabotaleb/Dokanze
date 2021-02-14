from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['name', 'parent']


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'parent')


class CategoryListSerializer(serializers.ModelSerializer):
    children = SubCategorySerializer(many=True, read_only=True)

    def get_children(self, obj):
        return obj.sub_category

    class Meta:
        model = Category
        fields = ['id', 'name', 'children']


class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ("modified",)


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = "__all__"

    def get_category(self, obj):
        serializer = CategoryListSerializer(obj.category.all(), many=True)
        return serializer.data

