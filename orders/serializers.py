from .models import Order
from rest_framework import serializers

class OrderSerializer(serializers.ModelSerializer):

    total_price = serializers.ReadOnlyField()

    class Meta:
        model = Order
        fields = (
            'id', 
            'user', 
            'product', 
            'price', 
            'amount',
            'date_of_order', 
            'payment_type',
            'total_price',
        )
        read_only_fields = ('id', 'date_of_order')