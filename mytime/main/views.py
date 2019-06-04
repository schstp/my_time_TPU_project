from datetime import datetime, timedelta
from django.views.generic import ListView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task, List
from django.http import JsonResponse


SMART_LISTS = {'inbox', 'today', 'tomorrow', 'week', 'starred', 'all'}

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'main/initial.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TaskListView, self).get_context_data()
        lists = List.objects.filter(user=self.request.user)
        context['lists'] = lists

        now = datetime.now().date()
        overdue_tasks = Task.objects.filter(planned_on__date__lt=now)
        count_overdue_tasks = overdue_tasks.count()

        inbox = Task.objects.filter(list=None)
        today = Task.objects.filter(planned_on__date=now) | overdue_tasks
        tomorrow = Task.objects.filter(planned_on__date=now + timedelta(days=1))
        week = Task.objects.filter(planned_on__date__gte=now, planned_on__date__lte=now + timedelta(days=7)) | overdue_tasks
        starred = Task.objects.filter(starred=True)
        all_tasks = Task.objects.filter(user=self.request.user)

        smart_lists = [
            {
                'name': 'Входящие',
                'slug': 'inbox',
                'tasks': inbox,
                'count_tasks': inbox.count(),
                'count_overdue_tasks': inbox.filter(planned_on__date__lt=now).count(),
             },
            {
                'name': 'Сегодня',
                'slug': 'today',
                'tasks': today,
                'count_tasks': today.count(),
                'count_overdue_tasks': count_overdue_tasks},
            {
                'name': 'Завтра',
                'slug': 'tomorrow',
                'tasks': tomorrow,
                'count_tasks': tomorrow.count(),
                'count_overdue_tasks': 0,
            },
            {
                'name': 'Неделя',
                'slug': 'week',
                'tasks': week,
                'count_tasks': week.count(),
                'count_overdue_tasks': count_overdue_tasks,
            },
            {
                'name': 'Отмеченные',
                'slug': 'starred',
                'tasks': starred,
                'count_tasks': starred.count(),
                'count_overdue_tasks': starred.filter(planned_on__date__lt=now).count(),
            },
            {
                'name': 'Все',
                'slug': 'all',
                'tasks': all_tasks,
                'count_tasks': all_tasks.count(),
                'count_overdue_tasks': count_overdue_tasks,
            },

        ]

        context['smart_lists'] = smart_lists
        return context

    context_object_name = 'tasks'


class SearchResultsView(ListView):
    template_name = 'main/initial.html'

    def get(self, request, *args, **kwargs):
        all_tasks = Task.objects.filter(user=self.request.user)
        q = self.request.GET.get("q")
        if q:
            all_tasks = all_tasks.filter(title__icontains=q)
        response = [{'id': task.id, 'title': task.title} for task in all_tasks]
        return JsonResponse(response, safe=False)


class AddNewTaskView(View):
    template_name = 'main/initial.html'

    def post(self, request, *args, **kwargs):
        title = self.request.POST.get('title')
        user = self.request.user
        list = self.request.POST.get('active_list')

        if list not in SMART_LISTS:
            task = Task.objects.create(user=user, title=title, list=list,starred=False)
        else:
            task = Task.objects.create(user=user, title=title, starred=False)

        if title.strip():
            task.save()

        response = {
            'id': task.id,
            'title': title,
            'list': list,
        }
        return JsonResponse(response, safe=False)
