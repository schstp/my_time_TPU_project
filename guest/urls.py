from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'guest-home'),
    path('blog/', views.blog, name = 'guest-blog'),
    path('support/', views.support, name = 'guest-support')
]