from django.db import models
from django.contrib.auth.models import User


class List(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class InboxList(List):
    pass


class Task(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    content = models.TextField()
    lists = models.ManyToManyField(List)
    timestemp = models.DateTimeField(auto_now_add = True, auto_now = False)


    def __str__(self):
        return self.content

    class Meta:
        ordering = ['-timestemp']
