from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    p_id = serializers.IntegerField()
    title = serializers.CharField(max_length=225)
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)  