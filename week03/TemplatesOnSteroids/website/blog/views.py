from django.shortcuts import render

from .models import BlogPost
# Create your views here.

def index(request):
    blogs = BlogPost.objects.all()
    return render(request, 'index.html', locals())

def detail_blog(request, name):
    return render(request, 'detail-blog.html', locals())

def create_blog(request):
    return render(request, 'create-blog.html', locals())
