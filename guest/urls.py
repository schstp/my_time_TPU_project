from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.home, name = 'guest-home'),
    path('blog/', views.blog, name = 'guest-blog'),
    path('support/', views.support, name = 'guest-support'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', views.login, name='registration-login'),
    path('accounts/logout/', views.logout, name='registration-logout'),
]