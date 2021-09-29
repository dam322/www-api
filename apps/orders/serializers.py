from rest_framework import serializers

from apps.orders.models import Order, OrderProduct, OrderProductIngredient
from apps.products.serializers import ProductSerializer, IngredientSerializer, VariationSerializer


class OrderProductIngredientSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer()
    variation = VariationSerializer()

    class Meta:
        model = OrderProductIngredient
        fields = '__all__'


class OrderProductIngredientCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProductIngredient
        fields = '__all__'
        extra_kwargs = {
            'order_product': {
                'read_only': True,
            }
        }


class OrderProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    ingredients = OrderProductIngredientSerializer(many=True)

    class Meta:
        model = OrderProduct
        fields = '__all__'


class OrderProductCreateSerializer(serializers.ModelSerializer):
    ingredients = OrderProductIngredientCreateSerializer(many=True)

    class Meta:
        model = OrderProduct
        fields = '__all__'
        extra_kwargs = {
            'order': {
                'read_only': True,
            }
        }


class OrderListSerializer(serializers.ModelSerializer):
    products = OrderProductSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'


class OrderCreateSerializer(serializers.ModelSerializer):
    products = OrderProductCreateSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        products = validated_data.pop('products')
        order = Order.objects.create(**validated_data)
        order.save()
        for product_data in products:
            ingredients = product_data.pop('ingredients')
            order_product = OrderProduct.objects.create(order=order, **product_data)
            order_product.save()
            for ingredient_data in ingredients:
                # TODO Falta verificar que todos los ingredientes estén en la petición
                # TODO Aún en duda de si es necesario
                if order_product.product.ingredients.get(id=ingredient_data['ingredient'].id):
                    ingredient = OrderProductIngredient.objects.create(order_product=order_product, **ingredient_data)
                    ingredient.save()
        return order
