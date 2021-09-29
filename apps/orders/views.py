from rest_framework import generics

from apps.orders.models import Order
from .serializers import OrderListSerializer, OrderCreateSerializer


class ListAllOrder(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer


class CreateOrder(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
