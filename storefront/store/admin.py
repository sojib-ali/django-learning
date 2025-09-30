from django.contrib import admin
from django.db.models import Count
from .models import Customer, Product, Order, OrderItem, Collection

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    ordering = ['first_name', 'last_name']
    search_fields = ['first_name']
    list_per_page = 10

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price', 'inventory_status', 'collection_title']
    list_editable = ['unit_price']
    list_per_page = 10
    list_select_related = ['collection']

    #to show some selected field
    def collection_title(self, product):
        return product.collection.title

    @admin.display(ordering = 'inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'Low'
        return 'Ok'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'placed_at', 'customer']

#to show calculated relational field
@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']

    @admin.display(ordering = 'products_count')
    def products_count(self, collection):
        return collection.products_count
    
    def get_queryset(self, request):    
        return super().get_queryset(request).annotate(
            products_count = Count('product')
        )

admin.site.register(OrderItem)


