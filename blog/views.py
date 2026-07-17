from django.shortcuts import render, redirect, get_object_or_404
from .forms import BlogForm
from .models import Blog


def index(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/index.html', {
        'blogs': blogs
    })


def blogs_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'blog/blog_detail.html', {
        'blog': blog,
    })


def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save()
            return redirect('blog_detail', blog_id=blog.id)
    else:
        form = BlogForm()

    return render(request, 'blog/blog_create.html', {
        'form': form,
    })


def blogs_edit(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_detail', blog_id=blog.id)
    else:
        form = BlogForm(instance=blog)

    return render(request, 'blog/blog_edit.html', {
        'blog': blog,
        'form': form,
    })


def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)

    if request.method == 'POST':
        blog.delete()
        return redirect('blog_index')

    return redirect('blog_detail', blog_id=blog.id)