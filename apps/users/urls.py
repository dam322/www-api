from django.contrib import admin
from django.urls import path
from .views import (
    Login, Logout, Signup, Account, Employess,
)

urlpatterns = [
    path('login/', Login.as_view()),
    path('logout/', Logout.as_view()),
    path('signup/', Signup.as_view()),
    path('account/<int:pk>', Account.as_view()),
    # Employees
    path('employees/', Employess.as_view()),
]
