from django.shortcuts import render
from .models import Project, Skill, Design

def index(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()  # Fetch skills from database
    designs = Design.objects.all()  # Fetch designs from database
    return render(request, 'index.html', {'projects': projects, 'skills': skills, 'designs': designs})
