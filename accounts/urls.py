from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth.views import auth_login



urlpatterns = [
    path('login/', views.login, name='registration-login'),
    path('logout/', views.logout, name='registration-logout'),
    path('signup/', views.SignUp, name='registration-signup'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),
]
