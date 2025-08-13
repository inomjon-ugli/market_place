from permissions import IsOwner
from .serializers import OrderSerializer
from .models import Order
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class OrderCrudModelViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsOwner,IsAuthenticated]


    def get_queryset(self):
        if self.request.user.is_staff:
            return Order.objects.all()
        return Order.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


