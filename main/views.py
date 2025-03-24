from django.shortcuts import render
from .models import Project, Skill

def index(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()  # Fetch skills from database
    return render(request, 'index.html', {'projects': projects, 'skills': skills})
