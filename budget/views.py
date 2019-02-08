from django.shortcuts import render, get_object_or_404
from .models import Project

def project_list(request):
    return render(request, 'project-list.html', {})

def project_detail(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)
    return render(request, 'project-detail.html', {'project': project})
