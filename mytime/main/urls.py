from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns = [
    path('', views.TaskListView.as_view(), name='index'),
    path('add_task', views.AddNewTaskView.as_view(), name='add_task'),
    path('search_query', views.SearchResultsView.as_view(), name='search_query'),
    path('active_list', views.ActiveListChangeView.as_view(), name='active_list'),
    path('archive_task', views.ArchiveTaskView.as_view(), name='archive_task'),
    path('add_list', views.AddNewListView.as_view(), name='add_list'),
    path('swap_starred', views.SwapStarredView.as_view(), name='swap_starred'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)