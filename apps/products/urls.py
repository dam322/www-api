from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from apps.products.views import (
    ProductList, ProductUpdateDestroy, ProductCreate
)

urlpatterns = [
    path('products/', ProductList.as_view()),
    path('product/', ProductCreate.as_view()),
    path('product/<int:pk>', ProductUpdateDestroy.as_view()),
    # TODO ProductIngredients
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
