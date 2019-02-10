from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from django.utils.text import slugify

from .models import Project, Category

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
        self.object = form.save(commit=False)
        self.object.save()

        categories = self.request.POST['categoriesString'].split(',')
        for category in categories:
            Category.objects.get_or_create(
                project = self.object,
                name = category
            )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return slugify(self.request.POST['name'])
