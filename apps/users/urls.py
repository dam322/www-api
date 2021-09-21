from django.contrib import admin
from django.urls import path
from .views import LoginAPIView, LogoutAPIView, SignupAPIView,AccountAPIView # , UserListView
urlpatterns = [
    path('login/', LoginAPIView.as_view()),
    # path('all/', UserListView.as_view())
    path('logout/', LogoutAPIView.as_view()),
    path('signup/', SignupAPIView.as_view()),
    path('account/<int:pk>', AccountAPIView.as_view()),
    # TODO UpdateAccount ##
    # TODO DeleteAccount
    # TODO Tokens Authorization
    # TODO SignupByAdministrator ##
]
