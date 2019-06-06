from django.views.generic import ListView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse

from .models import Task, List
from .core import get_filled_lists, get_filled_querysets, make_task, SMART_LISTS


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'main/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TaskListView, self).get_context_data()
        context.update(get_filled_lists(self.request.user))
        return context

    context_object_name = 'tasks'


class SearchResultsView(ListView):
    template_name = 'main/index.html'

    def get(self, request, *args, **kwargs):
        list_id = self.request.GET.get('active_list_id')
        q = self.request.GET.get('q')
        user = self.request.user
        all_tasks = get_filled_querysets(user)

        if q:
            if list_id in SMART_LISTS:
                all_tasks = all_tasks['smart_lists'][list_id]['tasks'].filter(title__icontains=q)
            else:
                all_tasks = List.objects.get(pk=int(list_id)).task_set.filter(title__icontains=q)

            response = [{'id': task.id, 'title': task.title} for task in all_tasks]
        else:
            if list_id in SMART_LISTS:
                all_tasks = all_tasks['smart_lists'][list_id]['tasks']
            else:
                all_tasks = List.objects.get(pk=int(list_id)).task_set.all()

            response = [{'id': task.id, 'title': task.title} for task in all_tasks]

        return JsonResponse(response, safe=False)


class AddNewTaskView(View):
    template_name = 'main/index.html'

    def post(self, request, *args, **kwargs):
        list_id = self.request.POST.get('active_list_id')

        task = make_task(self.request)
        if task.title.strip():
            task.save()

        response = {
            'id': task.id,
            'list_id': list_id,
            'title': task.title,
            'starred': task.starred,
            'planned_on': task.planned_on,
        }
        response.update(get_filled_lists(self.request.user))

        return JsonResponse(response, safe=False)


class ActiveListChangeView(View):
    template_name = 'main/index.html'

    def get(self, request, *args, **kwargs):
        list_id = self.request.GET.get('active_list_id')
        context = get_filled_lists(self.request.user)

        if list_id in SMART_LISTS:
            response = {
                'tasks': context['smart_lists'][list_id]['tasks'],
                'list_title': context['smart_lists'][list_id]['name'],
            }
        else:
            active_list = List.objects.get(pk=int(list_id))
            response = {
                'tasks': list(active_list.task_set.values()),
                'list_title': List.objects.get(pk=int(list_id)).title,
            }

        return JsonResponse(response, safe=False)


class ArchiveTaskView(View):
    template_name = 'main/index.html'

    def post(self, request, *args, **kwargs):
        list_id = self.request.POST.get('active_list_id')

        task = make_task(self.request)
        if task.title.strip():
            task.save()

        response = {
            'id': task.id,
            'list_id': list_id,
            'title': task.title,
            'starred': task.starred,
            'planned_on': task.planned_on,
        }
        response.update(get_filled_lists(self.request.user))

        return JsonResponse(response, safe=False)