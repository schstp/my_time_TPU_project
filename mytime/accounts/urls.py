from django.urls import path, include, re_path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('django.contrib.auth.urls')),
    path('signup/', views.SignUp, name='signup'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),
    path('edit/', views.edit, name='edit'),
]
