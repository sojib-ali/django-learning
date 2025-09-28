from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product

# Create your views here.
def say_hello(request):

    first_product = Product.objects.get(pk = 1)
    
    #instead of try catch
    product = Product.objects.get(pk = 0).first()

    #to know if a product exists - return a boolean
    exists = Product.objects.filter(pk=0).exists()


    return render(request, 'hello.html', {'name': 'sojib'})