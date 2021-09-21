from django.contrib import admin
from django.urls import path
from .views import LoginAPIView, LogoutAPIView, SignupAPIView  # , UserListView
urlpatterns = [
    path('login/', LoginAPIView.as_view()),
    # path('all/', UserListView.as_view())
    path('logout/', LogoutAPIView.as_view()),
    # TODO Signup ##
    path('signup/', SignupAPIView.as_view()),
    # TODO Account ##
    # TODO UpdateAccount ##
    # TODO DeleteAccount
    # TODO Tokens Authorization
    # TODO SignupByAdministrator ##
]
