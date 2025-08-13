
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # swager
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
   #  app urls

   path('api/v1/', include([
        path('users/', include('users.urls')),
        path('cards_of_users/', include('cards_of_users.urls')),
        path('cart/', include('cart.urls')),
        path('categories/', include('categories.urls')),
        path('images/', include('image_of_products.urls')),
        path('likes/', include('likes.urls')),
        path('orders/', include('orders.urls')),
        path('products/', include('products.urls')),
        path('stores/', include('stores.urls')),
    ])),
]
