from decimal import Decimal
from store.models import Product, Collection
from rest_framework import serializers


class CollectionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length = 255)

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField
    title = serializers.CharField(max_length = 255)
    price = serializers.DecimalField(max_digits=6, decimal_places=2, source = 'unit_price')
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    #getting relational field through nested object
    collection = CollectionSerializer()

    def calculate_tax(self, product):
        return product.unit_price * Decimal(1.1)