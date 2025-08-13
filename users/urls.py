from django.urls import path
from .views import RegisterCreateAPView, UsersListAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [

    # jwt token
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   
    # register
    path('register/',RegisterCreateAPView.as_view()),
    path('list/',UsersListAPIView.as_view())


]
