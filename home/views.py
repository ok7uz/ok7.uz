from django.shortcuts import render

from project.models import Project


def home_view(request):
    projects = Project.objects.all()
    return render(request, 'home.html', context={'projects': projects})
