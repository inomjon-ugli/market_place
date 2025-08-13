from .models import Users
from .serializers import RegisterUserSerializer, UserListSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser


class RegisterCreateAPView(generics.CreateAPIView):
    queryset = Users.objects.all()
    serializer_class=RegisterUserSerializer
    permission_class = [AllowAny]

class UsersListAPIView(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

