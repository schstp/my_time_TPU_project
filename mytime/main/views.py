from django.views.generic import ListView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task, List
from .core import get_filled_lists, get_filled_querysets, make_task, SMART_LISTS, TIME_FORMAT


import json
from datetime import datetime

from django.http import HttpResponse

class DateTimeEncoder(json.JSONEncoder):
    # default JSONEncoder cannot serialize datetime.datetime objects
    def default(self, obj):
        if isinstance(obj, datetime):
            encoded_object = obj.strftime(TIME_FORMAT)
        else:
            encoded_object = super(self, obj)
        return encoded_object

class JsonResponse(HttpResponse):
    def __init__(self, content, mimetype='application/json', status=None, content_type='application/json'):
        json_text = json.dumps(content, cls=DateTimeEncoder)
        super(JsonResponse, self).__init__(
            content=json_text,
            status=status,
            content_type=content_type)


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

            response = [{'id': task.id,
                         'title': task.title,
                         'starred': task.starred,
                         'planned_on': task.planned_on
                         } for task in all_tasks]
        else:
            if list_id in SMART_LISTS:
                all_tasks = all_tasks['smart_lists'][list_id]['tasks']
            else:
                all_tasks = List.objects.get(pk=int(list_id)).task_set.all()

            response = [{'id': task.id,
                         'title': task.title,
                         'starred': task.starred,
                         'planned_on': task.planned_on
                         } for task in all_tasks]

        return JsonResponse(response)


class AddNewTaskView(View):
    template_name = 'main/index.html'

    def post(self, request, *args, **kwargs):
        list_id = self.request.POST.get('active_list_id')

        task = make_task(self.request)
        task.save()

        response = {
            'id': task.id,
            'list_id': list_id,
            'title': task.title,
            'starred': task.starred,
            'planned_on': task.planned_on,
        }

        response.update(get_filled_lists(self.request.user))

        return JsonResponse(response)


class AddNewListView(View):
    template_name = 'main/index.html'

    def post(self, request, *args, **kwargs):
        user = self.request.user
        list_title = self.request.POST.get('list_title')
        new_personal_list = List.objects.create(user=user, title=list_title.strip())
        new_personal_list.save()

        response = {
            'id': new_personal_list.id,
            'title': new_personal_list.title,
        }

        return JsonResponse(response)


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
                'tasks': list(active_list.task_set.filter(archived=False).values()),
                'list_title': List.objects.get(pk=int(list_id)).title,
            }

        return JsonResponse(response)


class ArchiveTaskView(View):
    template_name = 'main/index.html'

    def post(self, request, *args, **kwargs):
        task_to_archive_id = self.request.POST.get('task_to_archive_id')
        task = Task.objects.get(pk=int(task_to_archive_id))
        task.archived = True
        task.save()

        response = get_filled_lists(self.request.user)

        return JsonResponse(response)


class SwapStarredView(View):
    template_name = 'main/index.html'

    def post(self, request, *args, **kwargs):
        user = self.request.user
        task_id = self.request.POST.get('task_id')
        starred = True if self.request.POST.get('starred') == 'true' else False

        task = Task.objects.get(pk=int(task_id))
        task.starred = starred
        task.save()

        response = get_filled_lists(user)['smart_lists']['starred']

        return JsonResponse(response)
