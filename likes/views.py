from .serializers import LikeSerializer
from .models import Like
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated



class LikeModelViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated] 


