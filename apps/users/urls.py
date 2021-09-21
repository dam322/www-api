from django.contrib import admin
from django.urls import path
from .views import LoginAPIView, LogoutAPIView, SignupAPIView, AccountAPIView, SignupByAdministratorAPIView

urlpatterns = [
    path('login/', LoginAPIView.as_view()),
    path('logout/', LogoutAPIView.as_view()),
    path('signup/', SignupAPIView.as_view()),
    path('account/<int:pk>', AccountAPIView.as_view()),
    path('signup/', SignupByAdministratorAPIView.as_view()),
    # TODO Listar empleados de un restaurante
]
