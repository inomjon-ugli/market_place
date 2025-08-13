from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import ImageProductSerializer
from .models import ProductImage


class ProductImageViewset(viewsets.ModelViewSet):
    serializer_class = ImageProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if getattr(self, 'swagger_fake_view', False) or not user.is_authenticated: #bu qator swagerda xato kelmasligi uchun
            return ProductImage.objects.none()
        return ProductImage.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)