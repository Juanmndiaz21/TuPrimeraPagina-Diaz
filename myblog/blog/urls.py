from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),


    path('post/new/', views.create_post, name='create_post'),
    path('author/new/', views.create_author, name='create_author'),
    path('authors/', views.author_list, name='author_list'),
    path('category/new/', views.create_category, name='create_category'),
    path('categories/', views.category_list, name='category_list'),
    path('search/', views.search_posts, name='search_posts'),
]