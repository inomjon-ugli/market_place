from .models import Users
from .serializers import RegisterUserSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny




class RegisterCreateAPView(generics.CreateAPIView):
    queryset = Users.objects.all()
    serializer_class=RegisterUserSerializer
    permission_class = [AllowAny]

