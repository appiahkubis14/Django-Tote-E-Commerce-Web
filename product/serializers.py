from rest_framework import serializers
from ..portal.models import Product, Cart, Order

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Cart
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    products = CartSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
