from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, Customer, Collection, Order, OrderItem

# Create your views here.
def say_hello(request):

    # first_product = Product.objects.get(pk = 1)
    
    # #instead of try catch
    # product = Product.objects.get(pk = 0).first()

    # #to know if a product exists - return a boolean
    # exists = Product.objects.filter(pk=0).exists()

    product = Product.objects.filter(inventory__lt=10)

    customer = Customer.objects.filter(id = 1)

    collection = Collection.objects.filter(featured_product__isnull = True)

    order = Order.objects.filter(customer__id=1)

    # order_item = OrderItem.objects.filter(product__collection__id=3)
    order_item = OrderItem.objects.all()

    # ordered_products = sorted({item.product.title for item in order_item})

    ordered_products = Product.objects.filter(id__in = OrderItem.objects.values('product_id').distinct()).order_by('title')
    



    return render(request, 'hello.html', {'name': 'sojib', 'products' : product, 'customers' : customer, 'orders': order, 'ordered_products': ordered_products})