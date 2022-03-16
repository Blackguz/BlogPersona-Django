from django.shortcuts import render, HttpResponse

# Create your views here.
def profile(request):
    return HttpResponse("<h1>Pagina de perfil</h1>")