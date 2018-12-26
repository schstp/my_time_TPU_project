from django.db import models
from django.contrib.auth.models import User


def mainImageFolder (article, filename):
    filename = 'main-' + article.slug + '.' + filename.split('.')[-1]
    return "{0}/{1}".format(article.slug, filename)

class Article (models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField()
    description = models.TextField()
    post = models.TextField()
    mainImage = models.ImageField(blank = True, upload_to = mainImageFolder)
    date = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    content = models.TextField()
    timestemp = models.DateTimeField(auto_now_add = True, auto_now = False)
    article = models.ForeignKey(Article, on_delete = models.CASCADE)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['-timestemp']