from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    content = models.TextField()
    timestemp = models.DateTimeField(auto_now_add = True, auto_now = False)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['-timestemp']
