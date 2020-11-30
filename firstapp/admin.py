from django.contrib import admin
from firstapp.models import PizzaShop, Pizza, Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ['pizza', 'name', 'phone', 'data']


admin.site.register(PizzaShop)
admin.site.register(Pizza)
admin.site.register(Order, OrderAdmin)
