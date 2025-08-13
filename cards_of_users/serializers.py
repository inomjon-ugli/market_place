from .models import Cards_of_users
from rest_framework import serializers



class CardUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cards_of_users
        fields = (
            'id',
            'user',
            'card_number',
            'expire_date',
        )
        read_only_fields = ['id','user']