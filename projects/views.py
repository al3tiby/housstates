from django.shortcuts import render
from django.views.generic import ListView
from . models import *

# Create your views here.

class ProjectsListView(ListView):
    model = Projects
    queryset = Projects.objects.all().order_by('-id')

    paginate_by = 4
    context_object_name = 'projects'
    template_name = 'projects/home.html'
