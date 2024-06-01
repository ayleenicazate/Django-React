from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CartViewSet, main

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'carts', CartViewSet)

urlpatterns = [
    path('home', main),
    path('', main)
]