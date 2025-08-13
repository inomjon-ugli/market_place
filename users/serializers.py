from rest_framework import serializers
from .models import Users

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = [
            'id',
            'username',   
            'email',
            'password',
            'role',
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            'role': {'read_only': True},
            'is_active': {'default': True}
        }

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = Users(**validated_data)
        user.set_password(password)  
        user.save()
        return user


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = (
            'id',
            'username', 
            'first_name',
            'last_name',  
            'email',
            'password',
            'phone',
            'address',
            'role',
            'is_active'
        )


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = (
            'username', 
            'first_name',
            'last_name',  
            'email',
            'password',
            'phone',
            'address',
        )



class ChangePasswordSerializer(serializers.Serializer):
    pass



class UserRoleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = (
            'id',
            'username',
            'role',
        )