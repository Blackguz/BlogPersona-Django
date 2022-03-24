from urllib import response
from django.shortcuts import render

#Models
from .models import Post

# Create your views here.

def posts(request):
    frist_post = Post.objects.first()
    posts =  Post.objects.all()
    return render(request, 'blogs.html', {'posts':posts, 'frist':frist_post})

def post(request, id):
    blog = Post.objects.get(id=id)
    return render(request, 'blog.html', {'post': blog})
