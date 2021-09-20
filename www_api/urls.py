from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('apps.users.urls')),
    # path('restaurants/', include('apps.restaurants.urls')),
    # path('orders/', include('apps.restaurants.urls')),
    # path('products/', include('apps.restaurants.urls')),
]
