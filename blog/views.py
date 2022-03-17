from django.shortcuts import render, HttpResponse

#Models
from .models import Post

# Create your views here.

def posts(request):
    blogs =  Post.objects.all()
    return HttpResponse('<h1>Pagina de publicaciones</h1>')

def post(request, id):
        return HttpResponse('<h1>Pagina de blog</h1>')
