from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProjectsListView.as_view(), name='projects'),

    path('create_project', views.create_project, name='create_project'),
    path('project/<int:pk>/', views.ProjectUpdateView.as_view(), name='update_project'),
]