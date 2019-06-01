from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
from django.shortcuts import get_list_or_404
from django.utils.functional import cached_property


class QuantitiesMixin:
    @cached_property
    def list_counts(self):
        return None


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'main/base.html'

    def get_queryset(self):
        queryset = get_list_or_404(Task, user=self.request.user)
        q = self.request.GET.get('q')
        if q:
            return queryset.filter(content__icontains=q)
        return queryset

    context_object_name = 'tasks'
