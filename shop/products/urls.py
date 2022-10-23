from django.urls import path
from . import views


urlpatterns = [
    path('products/get/', views.ProductListView.as_view()),
    path('products/get/<int:pk>/', views.ProductDetailView.as_view()),
    path('products/post/', views.ProductCreateView.as_view()),
    path('products/path/<int:pk>/', views.ProductUpdateView.as_view()),
    path('products/delete/<int:pk>/', views.ProductDestroyView.as_view()),

    path('category/get/', views.TypeProductListView.as_view()),
    path('category/get/<int:pk>/', views.TypeProductDetailView.as_view()),
    path('category/post/', views.TypeProductCreateView.as_view()),
    path('category/path/<int:pk>/', views.TypeProductUpdateView.as_view()),
    path('category/delete/<int:pk>/', views.TypeProductDestroyView.as_view()),
]