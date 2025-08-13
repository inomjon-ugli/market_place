from .serializers import ProductSerializer
from .models import Product
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser
from .permissions import IsAdminOrSeller, IsSeller



class ProductCrudModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny] 
    authentication_classes = [JWTAuthentication]

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny] 
        elif self.action == 'create':
            permission_classes = [IsAdminOrSeller] 
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsSeller]  
        else:
            permission_classes = [IsAuthenticated] 
        return [permission() for permission in permission_classes]


    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_object()
        serializer = self.get_serializer(queryset)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        queryset = self.get_object()
        serializer = self.get_serializer(queryset, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, *args, **kwargs):
        queryset = self.get_object()
        queryset.delete()
        return Response({"status":status.HTTP_204_NO_CONTENT})

