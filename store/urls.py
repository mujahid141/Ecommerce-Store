from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello),
    path('product/<int:id>/', views.product),  # Include the 'id' parameter in the URL
    path('products/', views.products),# Include the 'id' parameter in the URL
    
]
