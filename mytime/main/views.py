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
        return context

    context_object_name = 'tasks'
