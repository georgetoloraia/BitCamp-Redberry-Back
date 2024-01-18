from django.urls import path
from . import views

urlpatterns = [
    # Blog URLs
    path('blogs/', views.BlogListView.as_view(), name='blog-list'),
    path('blogs/create/', views.BlogCreateView.as_view(), name='blog-create'),
    path('blogs/<int:pk>/', views.BlogDetailView.as_view(), name='blog-detail'),

    # Category URLs
    path('categories/', views.CategoryListView.as_view(), name='category-list'),

    # User and Authentication URLs
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.UserCreateView.as_view(), name='user-register'),

]
