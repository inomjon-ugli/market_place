from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LikeModelViewSet

router = DefaultRouter()
router.register('', LikeModelViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
]