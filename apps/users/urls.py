from django.contrib import admin
from django.urls import path
from .views import (
    LoginAPIView, LogoutAPIView, SignupAPIView, AccountAPIView, ListEmployeesView,
    RestaurantRetrieveUpdateDestroyAPIView, RestaurantListAPIView, RestaurantCreateAPIView
)

urlpatterns = [
    path('login/', LoginAPIView.as_view()),
    path('logout/', LogoutAPIView.as_view()),
    path('signup/', SignupAPIView.as_view()),
    path('account/<int:pk>', AccountAPIView.as_view()),
    # Restaurants
    path('restaurants/', RestaurantListAPIView.as_view()),
    path('restaurant/create', RestaurantCreateAPIView.as_view()),
    path('restaurant/<int:pk>', RestaurantRetrieveUpdateDestroyAPIView.as_view()),
    path('list-employees/', ListEmployeesView.as_view()),
]
