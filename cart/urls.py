from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CartCrudModelViewSet

router = DefaultRouter()
router.register('', CartCrudModelViewSet, basename='store')

urlpatterns = [
    path('', include(router.urls)),
]