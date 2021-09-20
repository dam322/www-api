from django.contrib import admin
from django.urls import path
from .views import LoginView# , UserListView
urlpatterns = [
    # TODO Login ##
    path('login/', LoginView.as_view()),
    # path('all/', UserListView.as_view())
    # TODO Logout
    # TODO Signup ##
    # TODO Account ##
    # TODO UpdateAccount ##
    # TODO DeleteAccount
    # TODO Tokens Authorization
    # TODO SignupByAdministrator ##
]
