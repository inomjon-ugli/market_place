from permissions import IsOwner
from .serializers import CardUserSerializer
from rest_framework import viewsets
from .models import Cards_of_users
from rest_framework.permissions import AllowAny,IsAuthenticated

class CardUserCrudModelViewSet(viewsets.ModelViewSet):
    serializer_class = CardUserSerializer
    permission_classes = [IsAuthenticated,IsOwner]
    queryset = Cards_of_users.objects.all()

    def get_queryset(self):
        return Cards_of_users.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.action in ['list','create']:
            permission_classes = [IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'destroy', 'retrieve']:
            permission_classes = [IsAuthenticated,IsOwner]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]


