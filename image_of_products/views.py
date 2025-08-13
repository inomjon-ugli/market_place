from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from permissions import IsOwner
from .serializers import ImageProductSerializer
from .models import ProductImage

class ProductImageViewset(viewsets.ModelViewSet):
    serializer_class = ImageProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ProductImage.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        elif self.action in ['update', 'partial_update', 'destroy', 'create']:
            permission_classes = [IsOwner]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
