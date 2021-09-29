from django.urls import path
from .views import ListAllOrder, CreateOrder, RetrieveOrder

urlpatterns = [
    path('orders/', ListAllOrder.as_view()),
    path('order/', CreateOrder.as_view()),
    path('order/<int:pk>', RetrieveOrder.as_view()),
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
