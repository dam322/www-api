from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Product
from .serializers import ProductListSerializer
from ..users.models import Restaurant


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    permission_classes = (IsAuthenticated,)


class ProductUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProductListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        restaurant = get_object_or_404(Restaurant, administrator=self.request.user)
        product = get_object_or_404(restaurant.products, id=self.kwargs['pk'])
        return Product.objects.filter(id=product.id)


class ProductDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ProductListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        restaurant = get_object_or_404(Restaurant, administrator=self.request.user)
        product = get_object_or_404(restaurant.products, id=self.kwargs['pk'])
        return Product.objects.filter(id=product.id)


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
