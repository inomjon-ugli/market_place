from rest_framework import serializers
from .models import ProductImage




class ImageProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = (
            'id',
            'product',
            'image'
        )
        read_only_fields = ['id','product']