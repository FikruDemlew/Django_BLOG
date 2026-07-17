from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blog_index'),
    path('create/', views.blog_create, name='blog_create'),
    path('<int:blog_id>/', views.blogs_detail, name='blog_detail'),
    path('<int:blog_id>/edit/', views.blogs_edit, name='blog_edit'),
    path('<int:blog_id>/delete/', views.delete_blog, name='delete_blog'),
]
