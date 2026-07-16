
from django.urls import path
from . import views
# http://127.0.0.1:8000/blogs/
# http://127.0.0.1:8000/blogs/delete/
urlpatterns = [
    path('', views.index, name='blog_index'),
    path('<int:blog_id>/', views.blogs_detail, name='blog_detail'),
]
