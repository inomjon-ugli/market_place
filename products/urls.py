from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductCrudModelViewSet

router = DefaultRouter()
router.register('', ProductCrudModelViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
]