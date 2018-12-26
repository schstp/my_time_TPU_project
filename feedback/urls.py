from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.contactForm, name = 'guest-support'),
    path('thanks', views.thanks, name = 'thanks'),
]