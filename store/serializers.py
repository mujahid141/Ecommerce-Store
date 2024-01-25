from rest_framework import serializers
from store.models import Product
from decimal import Decimal

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['p_id', 'title', 'description', 'price', 'inventory', 'collection_id']
