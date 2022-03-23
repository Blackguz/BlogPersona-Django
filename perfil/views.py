from turtle import title
from django.shortcuts import render
#models
from .models import Project

# Create your views here.
def profile(request):
    project = Project.objects.all()
    return render(request, 'profile.html')