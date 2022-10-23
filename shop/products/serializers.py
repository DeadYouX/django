from rest_framework import serializers

from .models import Product, TypeProduct


class ProductListSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='category_name', read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'category')


class TypeProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeProduct
        fields = '__all__'


class ProductDetailListSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='category_name', read_only=True)

    class Meta:
        model = Product
        fields = "__all__"


class TypeProductDetailListSerializer(serializers.ModelSerializer):
    product = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)

    class Meta:
        model = TypeProduct
        fields = "__all__"


class ProductCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class TypeProductCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TypeProduct
        fields = '__all__'


class ProductUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class TypeProductUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TypeProduct
        fields = '__all__'


class ProductDestroySerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class TypeProductDestroySerializer(serializers.ModelSerializer):

    class Meta:
        model = TypeProduct
        fields = '__all__'
