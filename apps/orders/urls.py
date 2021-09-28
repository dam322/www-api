from django.contrib import admin
from django.urls import path
from .views import ListAllOrder
urlpatterns = [
    path('orders/', ListAllOrder.as_view()),
    # TODO CreateOrder
    # TODO CreateDetail // Contiene la información del producto pedido (precio, combinación de ingredientes, etc)
    # TODO UpdateDetail // Contiene la información del producto pedido (precio, combinación de ingredientes, etc)
    # TODO ListOrderDetails
    # TODO DeleteOrder
    # TODO OrdersQueue
    # TODO ConfirmOrderByCustomer
    # TODO UpdateOrderByEmployee
    # TODO UpdateOrder // ???
]
