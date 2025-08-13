from .serializers import CartSerializer
from .models import Cart
from rest_framework import viewsets





class CartCrudModelViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [] 
