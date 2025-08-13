from .serializers import OrderSerializer
from .models import Order
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated



class OrderCrudModelViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated] 


    def get_queryset(self):
        return Order.objects.filter(user=self.request.user) # hozirgi foydalanuvch buyurtmakari
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user) # user maydonini so‘rov qilayotgan foydalanuvchi bilan to‘ldirish
