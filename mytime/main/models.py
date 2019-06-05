from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, auto_now= False)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True


class List(TimeStampedModel):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']

    def count_tasks(self):
        return self.task_set.count()

    def count_overdue_tasks(self):
        return self.task_set.filter(planned_on__date__lt=datetime.now().date()).count()

    def __str__(self):
        return self.title


class Task(TimeStampedModel):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.TextField()
    list = models.ForeignKey(List, null=True, blank=True, on_delete=models.CASCADE)
    starred = models.BooleanField(default=False)
    planned_on = models.DateTimeField(blank=True, null=True)

    NONE_PRIORITY = 0
    LOW_PRIORITY = 1
    MIDDLE_PRIORITY = 2
    HIGH_PRIORITY = 3
    PRIORITY_LVL_CHOICES = (
        (NONE_PRIORITY, 'not specified'),
        (LOW_PRIORITY, 'green'),
        (MIDDLE_PRIORITY, 'yellow'),
        (HIGH_PRIORITY, 'red'),
    )
    priority_lvl = models.IntegerField(choices=PRIORITY_LVL_CHOICES, default=NONE_PRIORITY)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title
