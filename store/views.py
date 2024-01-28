from rest_framework.exceptions import ValidationError
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer

# Create your views here.

@api_view(['GET' , 'POST'])  # Specify the allowed HTTP methods (e.g., GET)
def hello(request):
    return Response("ok")

@api_view(['GET' , 'POST','DELETE'])  # Specify the allowed HTTP methods (e.g., GET)
def product(request, id):
    if request.method == 'GET':
        product = Product.objects.get(pk=id)
        serializer =  ProductSerializer(product)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    
        
        
@api_view(['GET' , 'POST'])  # Specify the allowed HTTP methods (e.g., GET)
def products(request):
    if request.method == 'GET':
        queryset = Product.objects.filter(price=10)
        serializer =  ProductSerializer(queryset, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Ok')
        

@api_view(['POST'])
def postProduct(request):
    serializer = ProductSerializer(data=request.data)
    try:
        serializer.is_valid(raise_exception=True)
    except ValidationError as e:
        return Response({'error': e.detail}, status=status.HTTP_400_BAD_REQUEST)

    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
