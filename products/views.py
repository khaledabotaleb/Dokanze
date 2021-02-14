from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    DestroyAPIView,
)

from .models import Category, Product
from .serializers import CategorySerializer ,CategoryListSerializer, CreateProductSerializer, ProductSerializer


# Create your views here.


class AddCategory(CreateAPIView):
    serializer_class = CategorySerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ListCategories(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class AddProduct(CreateAPIView):
    serializer_class = CreateProductSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ListProducts(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class GetProductsByCategory(APIView):
    serializer_class = ProductSerializer

    def get(self, request, cat_id):
        try:
            category = Category.objects.get(id=int(cat_id))
        except Category.DoesNotExist:
            return Response(
                {'error': 'category does not exist'},
                status=status.HTTP_404_NOT_FOUND
            )
        queryset = category.product_category.all()
        product_serializer = ProductSerializer(queryset, many=True)
        return Response(product_serializer.data, status=status.HTTP_200_OK)


class DeleteCategoryById(DestroyAPIView):
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"detail": "Category deleted"})