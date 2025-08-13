from .models import Like
from rest_framework import serializers

class LikeSerializer(serializers.ModelSerializer):


    class Meta:
        model = Like
        fields = (
            'id', 
            'user', 
            'product', 
            'created_at', 
            
        )
        read_only_fields = ('id', 'created_at','user',)
