from django.db import models

from apps.products.models import Ingredient, Variation, Product
from apps.users.models import User


class Order(models.Model):
    timestamp = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return f"{self.user.full_name} - {self.timestamp}"


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='details')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')


class OrderProductDetail(models.Model):
    order_product = models.ForeignKey(OrderProduct, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    variation = models.ForeignKey(Variation, on_delete=models.CASCADE, null=True, blank=True)
