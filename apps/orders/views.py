from rest_framework import generics

from apps.orders.models import Order
from .serializers import OrderListSerializer, OrderCreateSerializer


class ListAllOrder(generics.ListAPIView):
    serializer_class = OrderListSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class RetrieveOrder(generics.RetrieveAPIView):
    serializer_class = OrderListSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user, id=self.kwargs['pk'])


class CreateOrder(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
