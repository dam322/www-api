from django.contrib import admin

# Register your models here.
from apps.products.models import Product, Ingredient, Variation


class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = (IngredientInline,)
    list_filter = ('name', 'is_customizable')
    list_display = ('name', 'is_customizable')


class OptionInline(admin.TabularInline):
    model = Variation
    extra = 1


class IngredientAdmin(admin.ModelAdmin):
    inlines = (OptionInline,)
    list_filter = ('name', 'product', 'is_available', 'is_obligatory')
    list_display = ('name', 'product', 'is_available', 'is_obligatory')


admin.site.register(Product, ProductAdmin)
admin.site.register(Ingredient, IngredientAdmin)
