from django.urls import path

from apps.products.views import ProductListCurrentUser, ProductListByRestaurant

urlpatterns = [
    # TODO CreateProduct
    # TODO Deleteproduct
    # TODO Updateproduct
    path('list-products/', ProductListCurrentUser.as_view()),
    path('list-products/<int:pk>', ProductListByRestaurant.as_view())
    # TODO ProductIngredients
]
