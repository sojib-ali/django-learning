from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, Customer, Collection, Order, OrderItem
from django.db.models.aggregates import Count, Max, Min, Avg, Sum

# Create your views here.
def say_hello(request):

    # first_product = Product.objects.get(pk = 1)
    
    # #instead of try catch
    # product = Product.objects.get(pk = 0).first()

    # #to know if a product exists - return a boolean
    # exists = Product.objects.filter(pk=0).exists()

    # product = Product.objects.filter(inventory__lt=10)

    # customer = Customer.objects.filter(id = 1)

    # collection = Collection.objects.filter(featured_product__isnull = True)

    # order = Order.objects.filter(customer__id=1)

    # order_item = OrderItem.objects.filter(product__collection__id=3)
    order_item = OrderItem.objects.all()

    # ordered_products = sorted({item.product.title for item in order_item})

    ordered_products = Product.objects.filter(id__in = OrderItem.objects.values('product_id').distinct()).order_by('title')
    

    

    # return render(request, 'hello.html', {'name': 'sojib', 'products' : product, 'customers' : customer, 'orders': order, 'ordered_products': ordered_products})

    #select_related(1)
    Product.objects.select_related('collection').all()

     #prefetch_related(n)
    Product.objects.prefetch_related('promotions').select_related('collection').all()

    # queryset = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]

    #last 5 order
    last_order = Order.objects.select_related('customer').prefetch_related('order_items__product').order_by('-placed_at')[:5]



    result = Product.objects.aggregate(count = Count('id'), min_price = Min('unit_price'))

    order_quantity = Order.objects.aggregate(count = Count('id'))

    # number of products 1 have shold
    sold_item = OrderItem.objects.filter(product__id=1).aggregate(unit_sold = Sum('quantity'))

    # how many orders has customer 1 placed?
    order_by_customer_1 = Order.objects.filter(customer__id = 1).aggregate(order_count = Count('id'))

    #what is the min, max and average price of the product in collection 3
    price = Product.objects.filter(collection__id=3).aggregate(
        min_price=Min('unit_price'),
        avg_price=Avg('unit_price'),
        max_price=Max('unit_price')
    )
    
    return render(request, 'hello.html', {'name': 'sojib', 'result': result, 'order_quantity': order_quantity, 'last_orders': list(last_order), 'units_sold':sold_item, 'customer_order': order_by_customer_1, 'price': price })

#how to insert values
def insert_value(request):
    collection = Collection()
    collection.title = 'Video Games'
    collection.featured_product = Product(pk=1)
    collection.save()

#or
    Collection.objects.create(name = 'a', featured_product_id = 1)


# how