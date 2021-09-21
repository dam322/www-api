from rest_framework import serializers

from .models import Product, Ingredient, Variation


class VariationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Variation
        fields = '__all__'


class IngredientSerializer(serializers.ModelSerializer):
    variations = VariationSerializer(many=True)

    class Meta:
        model = Ingredient
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
