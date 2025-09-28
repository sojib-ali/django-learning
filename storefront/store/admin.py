from django.contrib import admin
from .models import Customer, Product, Order, OrderItem

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']
    search_fields = ['first_name', 'email']
    list_per_page = 10


admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)

