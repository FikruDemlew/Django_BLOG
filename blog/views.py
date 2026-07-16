from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog
# Create your views here.
def index(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/index.html', {
        'blogs': blogs
    })

def blogs_detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    return render(request, 'blog/blog_detail.html', {
        'blog': blog
    })