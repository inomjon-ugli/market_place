from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryCrudModelViewSet

router = DefaultRouter()
router.register('', CategoryCrudModelViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls)),
]