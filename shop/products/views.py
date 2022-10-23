from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from .models import Product, TypeProduct
from .serializers import ProductListSerializer, ProductDetailListSerializer, ProductCreateSerializer, \
    TypeProductListSerializer, TypeProductDetailListSerializer, TypeProductCreateSerializer, ProductUpdateSerializer, \
    TypeProductUpdateSerializer, ProductDestroySerializer, TypeProductDestroySerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailListSerializer


class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductCreateSerializer


class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductUpdateSerializer


class ProductDestroyView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDestroySerializer


class TypeProductListView(generics.ListAPIView):
    queryset = TypeProduct.objects.all()
    serializer_class = TypeProductListSerializer


class TypeProductDetailView(generics.RetrieveAPIView):
    queryset = TypeProduct.objects.all()
    serializer_class = TypeProductDetailListSerializer


class TypeProductCreateView(generics.CreateAPIView):
    serializer_class = TypeProductCreateSerializer


class TypeProductUpdateView(generics.UpdateAPIView):
    queryset = TypeProduct.objects.all()
    serializer_class = TypeProductUpdateSerializer


class TypeProductDestroyView(generics.DestroyAPIView):
    queryset = TypeProduct.objects.all()
    serializer_class = TypeProductDestroySerializer

