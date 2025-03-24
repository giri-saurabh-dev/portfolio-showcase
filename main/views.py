from django.shortcuts import render
from .models import Project

def index(request):
    projects = Project.objects.all()
    
    for project in projects:
        project.technologies_list = project.technologies.split(",")  # Create a new list attribute
    
    return render(request, 'index.html', {'projects': projects})
