from django.contrib import admin
from .models import *
# Register your models here.


class PriceInlineAdmin(admin.TabularInline):
    model = Price
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    inlines = [PriceInlineAdmin]

admin.site.register(Product, ProductAdmin)
# admin.site.register(Product)
admin.site.register(Price)