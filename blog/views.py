from django.shortcuts import render
from blog.models import Articles

def blog(request):

    context = {
        'title': 'Blog',
        'posts': Articles.objects.all().order_by("-date"),
    }
    return render(request, 'blog/overview.html', context)

def article_detail(request, pk):

    context = {
        'title': 'Blog',
        'article': Articles.objects.get(id = pk),
    }
    return render(request, 'blog/article.html', context)