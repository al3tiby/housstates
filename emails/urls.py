from django.urls import path
from . import views


urlpatterns = [
    path('contact_us/', views.contact_us, name='contact'),
    path('newsletter/', views.newsletteremails, name='newsletter'),
    path('newsletter_sender/', views.newsletter_senders, name='newsletter_sender')
]