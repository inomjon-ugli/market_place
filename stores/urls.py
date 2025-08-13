from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StoreCrudModelViewSet

router = DefaultRouter()
router.register('', StoreCrudModelViewSet, basename='store')

urlpatterns = [
    path('', include(router.urls)),
]