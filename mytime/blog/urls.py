from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static


from . import views


urlpatterns = [
    path('', views.blog, name = 'guest-blog'),
    re_path(r'^(?P<pk>\d+)/', views.article_detail, name='blog-post'),
    path('add_comment', views.CreateCommentView.as_view(), name='add_comment'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)