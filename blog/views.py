from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import *

# Create your views here.


class BlogsListView(ListView):
    model = Blog
    queryset = Blog.objects.all().order_by('-id')

    paginate_by = 9
    context_object_name = 'blogs'
    template_name = 'blog/blogs.html'


class BlogDetailView(DetailView):
    model = Blog
    queryset = Blog.objects.order_by('id')

    context_object_name = 'blog'
    template_name = 'blog/bolg_page.html'

