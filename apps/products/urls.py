from django.urls import path

from apps.products.views import (
    ProductListCurrentUser, ProductListByRestaurant,
    ProductUpdateAPIView, ProductDestroyAPIView, ProductCreateAPIView
)

urlpatterns = [
    path('product/', ProductCreateAPIView.as_view()),
    path('product/<int:pk>', ProductUpdateAPIView.as_view()),
    path('product/delete/<int:pk>', ProductDestroyAPIView.as_view()),
    path('list-products/', ProductListCurrentUser.as_view()),
    path('list-products/<int:pk>', ProductListByRestaurant.as_view())
    # TODO ProductIngredients
]
