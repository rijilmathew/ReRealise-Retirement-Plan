from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from .serializers import UserCreateSerializer, UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model

User = get_user_model()


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        token['is_superuser'] = user.is_superuser
        token['is_service_provider'] = user.is_service_provider
        
        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    

class UserRegisterView(APIView):
    def post(self, request):
        data = request.data
        
        serializer = UserCreateSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
        user = serializer.create(serializer.validated_data)
        user = UserSerializer(user)

        return Response(user.data, status = status.HTTP_201_CREATED)


class UserRetrieveView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        user = request.user
        user = UserSerializer(user)

        return Response(user.data, status = status.HTTP_200_OK)
 
