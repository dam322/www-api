from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializers import ProductListSerializer
from ..users.models import Restaurant


class ProductListCurrentUser(generics.ListAPIView):
    serializer_class = ProductListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        restaurant = get_object_or_404(Restaurant, administrator=self.request.user)
        return restaurant.products


class ProductListByRestaurant(generics.ListAPIView):
    serializer_class = ProductListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        restaurant = get_object_or_404(Restaurant, id=self.kwargs['pk'])
        return restaurant.products
