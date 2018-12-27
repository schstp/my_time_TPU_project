from django.urls import path, include, re_path
from . import views
from django.contrib.auth import login, logout



urlpatterns = [
    path('login/', login, name='registration-login'),
    path('logout/', logout, name='registration-logout'),
    path('signup/', views.SignUp, name='registration-signup'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),
]
