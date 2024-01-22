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

@api_view(['GET' , 'POST'])  # Specify the allowed HTTP methods (e.g., GET)
def product(request, id):
    if request.method == 'GET':
        product = Product.objects.get(pk=id)
        serializer =  ProductSerializer(product)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        
@api_view(['GET' , 'POST'])  # Specify the allowed HTTP methods (e.g., GET)
def products(request):
    if request.method == 'GET':
        queryset = Product.objects.filter(price=10)
        serializer =  ProductSerializer(queryset, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data
            return Response('Ok')
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST )
@api_view(['POST'])
def postProduct(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        # Process the data, save to database, etc.
        return Response({"message": "Product created successfully"}, status=201)
    return Response(serializer.errors, status=400)
