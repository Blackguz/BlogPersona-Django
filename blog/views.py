from urllib import response
from django.shortcuts import render

#Models
from .models import Post

# Create your views here.

def posts(request):
    blogs =  Post.objects.all()
    return render(request, 'blogs.html')

def post(request, id):
    #blog = Post.objects.get(id)
    #content = f'{blog.title} - {blog.descriptcion}'
    return render(request, 'blog.html')
