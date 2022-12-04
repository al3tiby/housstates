from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView
from . import models, forms
# Create your views here.


class BlogsListView(ListView):
    model = models.Blog
    queryset = model.objects.all().order_by('-id')

    paginate_by = 9
    context_object_name = 'blogs'
    template_name = 'blog/blogs.html'


class BlogDetailView(DetailView):
    model = models.Blog
    queryset = model.objects.order_by('id')

    context_object_name = 'blog'
    template_name = 'blog/bolg_page.html'



@user_passes_test((lambda u: u.is_superuser), 'admin_login')
def create_blog(request):
    if request.method == 'POST':
        title = request.POST['title']
        short_description = request.POST['short_description']
        description = request.POST['description']
        image = request.FILES['image']

        save_new_blog = models.Blog.objects.create(
            title=title,
            short_description=short_description,
            description=description,
            image=image
        )

        save_new_blog.save()
        created_done = save_new_blog
        context = {
            'created_done': created_done
        }
        return render(request, 'blog/create_blog.html', context)
    else:
        return render(request, 'blog/create_blog.html', {})



class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Blog
    form_class = forms.BlogUpdateForm
    template_name = 'blog/update_blog.html'

    def get_success_url(self):
        return reverse('control_panel')
