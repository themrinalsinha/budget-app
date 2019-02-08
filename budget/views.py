from django.shortcuts import render

def project_list(request):
    return render(request, 'project-list.html', {})

def project_detail(request, project_slug):
    return render(request, 'project-detail.html', {})

