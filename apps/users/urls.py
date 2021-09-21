from django.contrib import admin
from django.urls import path
from .views import (
    LoginAPIView, LogoutAPIView, SignupAPIView, AccountAPIView, ListEmployeesView,
    RestaurantRetrieveUpdateDestroyAPIView, RestaurantListCreateAPIView
)

urlpatterns = [
    path('login/', LoginAPIView.as_view()),
    path('logout/', LogoutAPIView.as_view()),
    path('signup/', SignupAPIView.as_view()),
    path('account/<int:pk>', AccountAPIView.as_view()),
    # Restaurants
    path('restaurant/', RestaurantListCreateAPIView.as_view()),
    path('restaurant/<int:pk>', RestaurantRetrieveUpdateDestroyAPIView.as_view()),
    # TODO Buscar restaurantes
    path('list-employees/', ListEmployeesView.as_view()),
]
