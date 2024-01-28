from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello),
    path('product/<int:id>/', views.ProductDetails.as_view()),  # Include the 'id' parameter in the URL
    path('products/', views.ProductList.as_view()),# Include the 'id' parameter in the URL
    path('postData/', views.postProduct),
]
