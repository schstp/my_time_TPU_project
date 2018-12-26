from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns = [
    path('', views.home, name = 'guest-home'),
    path('blog/', include('blog.urls')),
    path('support/', include(('feedback.urls'))),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', views.login, name='registration-login'),
    path('accounts/logout/', views.logout, name='registration-logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
