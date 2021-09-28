from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Product
from .serializers import ProductListSerializer


class ProductCreate(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    permission_classes = (IsAuthenticated,)


class ProductUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()
    permission_classes = (IsAuthenticated,)


class ProductList(generics.ListAPIView):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()
    permission_classes = (IsAuthenticated,)
