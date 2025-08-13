from .serializers import CardUserSerializer
from .models import Cards_of_users
from rest_framework import viewsets





class CardUserCrudModelViewSet(viewsets.ModelViewSet):
    queryset = Cards_of_users.objects.all()
    serializer_class = CardUserSerializer
    permission_classes = [] 
