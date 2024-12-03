# from rest_framework.routers import DefaultRouter
# from .views import ProductViewSet
# from django.urls import path, include


# router = DefaultRouter()
# router.register(r'products', ProductViewSet, basename='product')

# urlpatterns = [
#     path('', include(router.urls)),
# ]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

# Create a router and register the ProductViewSet
router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),  # Include the router's URLs
]

