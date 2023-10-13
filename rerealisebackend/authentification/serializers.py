from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password



User = get_user_model()

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'is_staff', 'is_active', 'is_doctor', 'phone_number')

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            password=make_password(validated_data['password']),
            phone_number=validated_data.get('phone_number'), 
        )
        
        return user



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_staff', 'is_active', 'is_doctor', 'is_superuser', 'phone_number') 