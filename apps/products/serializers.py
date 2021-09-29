from rest_framework import serializers

from .models import Product, Ingredient, Variation


class VariationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variation
        fields = '__all__'


class IngredientListSerializer(serializers.ModelSerializer):
    variations = VariationSerializer(many=True)

    class Meta:
        model = Ingredient
        fields = '__all__'


class IngredientSerializer(serializers.ModelSerializer):
    has_variations = serializers.BooleanField()

    class Meta:
        model = Ingredient
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    ingredients = IngredientListSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
