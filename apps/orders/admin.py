from django.contrib import admin

# Register your models here.
from apps.orders.models import OrderProduct, Order, OrderProductIngredient


class OrderProductIngredientInline(admin.TabularInline):
    model = OrderProductIngredient

    def get_queryset(self, request):
        qs = super(OrderProductIngredientInline, self).get_queryset(request)
        return qs


class OrderProductInline(admin.TabularInline):
    model = OrderProduct


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderProductInline,)


class OrderProductAdmin(admin.ModelAdmin):
    inlines = (OrderProductIngredientInline,)


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct, OrderProductAdmin)
