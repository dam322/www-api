from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.users.urls')),
    # path('orders/', include('apps.restaurants.urls')),
    # path('products/', include('apps.restaurants.urls')),
]
