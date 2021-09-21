from django.contrib import admin

# Register your models here.
from apps.users.models import User, Restaurant

admin.site.register(User)
admin.site.register(Restaurant)
