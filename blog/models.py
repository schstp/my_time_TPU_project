from django.db import models

def imageFolder (article, filename):
    filename = article.slug + '.' + filename.split('.')[-1]
    return "{0}/{1}".format(article.slug, filename)

class Articles (models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField()
    description = models.TextField()
    post = models.TextField()
    image = models.ImageField(blank = True, upload_to = imageFolder)
    date = models.DateTimeField()

    def __str__(self):
        return self.title