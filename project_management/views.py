from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required, user_passes_test
from projects.models import Projects
from blog.models import Blog



@user_passes_test((lambda u: u.is_superuser), 'admin_login')
def admin_lists(request):
    projects = Projects.objects.all().order_by('-id')
    paginator = Paginator(projects, 3)
    page = request.GET.get('project_page')
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)


    blogs = Blog.objects.all().order_by('-id')
    paginator = Paginator(blogs, 3)
    page = request.GET.get('blog_page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)


    context = {
        'projects': projects,
        'blogs': blogs
    }
    return render(request, 'admin/control_panel.html', context)
