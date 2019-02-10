from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView

from .models import Project

def project_list(request):
    return render(request, 'project-list.html', {})

def project_detail(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)
    return render(request, 'project-detail.html', {'project': project})

class ProjectCreateView(CreateView):
    model = Project
    template_name = 'add-project.html'
    fields = ('name', 'budget')

    def form_valid(self, form):
        import pdb; pdb.set_trace()
        self.object = form.save(commit=False)
        self.object.save()


