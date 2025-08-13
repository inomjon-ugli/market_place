from .serializers import CategorySerializer
from .models import Category
from rest_framework import viewsets
from rest_framework import permissions




class CategoryCrudModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]



    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [permissions.AllowAny]
        elif self.action in ['update', 'partial_update', 'destroy', 'create']:
            permission_classes = [permissions.IsAdminUser]  
        else:
            permission_classes = [permissions.IsAuthenticated] 
        return [permission() for permission in permission_classes]
