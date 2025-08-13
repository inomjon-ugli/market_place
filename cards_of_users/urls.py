from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CardUserCrudModelViewSet

router = DefaultRouter()
router.register('', CardUserCrudModelViewSet, basename='store')

urlpatterns = [
    path('', include(router.urls)),
]