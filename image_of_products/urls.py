from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductImageViewset

router = DefaultRouter()
router.register('', ProductImageViewset, basename='store')

urlpatterns = [
    path('', include(router.urls)),
]