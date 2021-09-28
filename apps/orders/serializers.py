from rest_framework import serializers

from apps.orders.models import Order, OrderProduct, OrderProductIngredient
from apps.products.serializers import ProductSerializer


class OrderProductIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProductIngredient
        fields = '__all__'


class OrderProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    ingredients = OrderProductIngredientSerializer(many=True)

    class Meta:
        model = OrderProduct
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    products = OrderProductSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'
