from django.urls import path
from . import views


urlpatterns = [
    path('', views.BlogsListView.as_view(), name='blogs'),
    path('<int:pk>/', views.BlogDetailView.as_view(), name='blog_page')
]