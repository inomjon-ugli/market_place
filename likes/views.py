from permissions import IsOwner
from .serializers import LikeSerializer
from .models import Like
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class LikeModelViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        if self.request.user.is_staff:
            return Like.objects.all()
        return Like.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsOwner, IsAdminUser]
        elif self.action in ['update', 'partial_update', 'destroy', 'create']:
            permission_classes = [IsOwner]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


