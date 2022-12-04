from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns = [
    path('', views.BlogsListView.as_view(), name='blogs'),
    path('<int:pk>/', views.BlogDetailView.as_view(), name='blog_page'),

    path('create_blog/', views.create_blog, name='create_blog'),
    path('update_blog/<int:pk>/', views.BlogUpdateView.as_view(), name='update_blog'),
]