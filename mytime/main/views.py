from datetime import datetime, timedelta
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task, List


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'main/initial.html'

    def get_queryset(self):
        queryset = Task.objects.filter(user=self.request.user)
        q = self.request.GET.get('q')
        if q:
            return queryset.filter(title__icontains=q)
        return queryset

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
        ]

        context['smart_lists'] = smart_lists
        return context

    context_object_name = 'tasks'
