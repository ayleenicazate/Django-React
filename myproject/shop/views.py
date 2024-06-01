from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Product, Cart
from .serializers import ProductSerializer, CartSerializer
from django.http import HttpResponse
from django.template import loader

def main(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def shop(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())


#serializadores DRF
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer