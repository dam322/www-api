from rest_framework import generics

from apps.orders.models import Order
from .serializers import OrderSerializer


class ListAllOrder(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
