from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=32)
    is_customizable = models.BooleanField()
    is_available = models.BooleanField()
    price = models.IntegerField()
    photo = models.ImageField(upload_to='products')

    def __str__(self):
        return f"{self.name}"


class Ingredient(models.Model):
    name = models.CharField(max_length=32)
    order = models.IntegerField()
    is_available = models.BooleanField()
    is_obligatory = models.BooleanField()
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, related_name='ingredients')

    @property
    def has_variations(self):
        return self.variations.exists()

    def __str__(self):
        return f"{self.name} - {self.product.name}"


class Variation(models.Model):
    name = models.CharField(max_length=32)
    is_available = models.BooleanField()
    ingredient = models.ForeignKey(to=Ingredient, on_delete=models.CASCADE, related_name='variations')

    def __str__(self):
        return f"{self.name} - {self.ingredient.name}"
