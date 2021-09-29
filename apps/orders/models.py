from django.db import models

from apps.products.models import Ingredient, Variation, Product
from apps.users.models import User


# TODO Verificar que cuando se cree una order y sus detalles la combinación de elementos sea válida
class Order(models.Model):
    class OrderStatus(models.Choices):
        ORDERED = 'ordered'
        IN_PROCESS = 'in process'
        PENDING = 'pending'

    timestamp = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(choices=OrderStatus.choices, default=OrderStatus.PENDING, blank=True, max_length=16)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return f"{self.user.full_name} - {self.timestamp}"


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.name} - {self.order.user} - {self.order.status}"


class OrderProductIngredient(models.Model):
    order_product = models.ForeignKey(OrderProduct, on_delete=models.CASCADE, related_name='ingredients')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    variation = models.ForeignKey(Variation, on_delete=models.CASCADE, null=True, blank=True)
