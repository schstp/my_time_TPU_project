from django.db import models
from django.contrib.auth.models import User


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, auto_now= False)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True


class List(TimeStampedModel):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


class Task(TimeStampedModel):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.TextField()
    lists = models.ForeignKey(List, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title
