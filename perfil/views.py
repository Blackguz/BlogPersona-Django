from turtle import title
from django.shortcuts import render, HttpResponse
#models
from .models import Project

# Create your views here.
def profile(request):
    project = Project.objects.all()
    
    return HttpResponse(project)