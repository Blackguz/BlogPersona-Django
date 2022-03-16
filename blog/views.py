from django.shortcuts import render, HttpResponse

# Create your views here.

def posts(request):
    return HttpResponse('<h1>Pagina de publicaciones</h1>')

def post(request, id):
        return HttpResponse('<h1>Pagina de blog</h1>')
