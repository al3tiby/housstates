from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import ListView, UpdateView, DeleteView
from .models import *
from .forms import *

# Create your views here.

class ProjectsListView(ListView):
    model = Projects
    queryset = Projects.objects.all().order_by('-id')

    paginate_by = 4
    context_object_name = 'projects'
    template_name = 'projects/home.html'



@user_passes_test((lambda u: u.is_superuser), 'admin_login')
def create_project(request):
    if request.method == 'POST':
        title = request.POST['title']
        short_description = request.POST['short_description']
        image = request.FILES['image']

        save_new_project = Projects.objects.create(
            title=title,
            short_description=short_description,
            image=image
        )

        save_new_project.save()
        created_done = save_new_project
        context = {
            'created_done': created_done
        }
        return render(request, 'projects/create_project.html', context)
    else:
        return render(request, 'projects/create_project.html', {})


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Projects
    form_class = ProjectUpdateForm
    template_name = 'projects/update_project.html'

    def get_success_url(self):
        return reverse('control_panel')


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Projects
    template_name = "projects/confirm_delete.html"

    def get_success_url(self):
        return reverse('control_panel')





