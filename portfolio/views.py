from django.shortcuts import render
from .models import Project  # импортируем Модели из нашего проекта Project

def home(request):
    projects = Project.objects.all()  # импортируем ВСЕ объекты из Project
    return render(request, 'portfolio/home.html', {'projects':projects})
