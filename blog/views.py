from django.shortcuts import render
from blog.models import Article
from blog.forms import CommentForm
from django.views import View
from django.core.paginator import Paginator
from django.http import JsonResponse

def blog(request):
    posts = Article.objects.all()
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()
    if page.has_previous():
        previous_url = "?page={}".format(page.previous_page_number())
    else:
        previous_url = ''

    if page.has_next():
        next_url = "?page={}".format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'title': 'Blog',
        'page_object': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'previous_url': previous_url,
    }
    return render(request, 'blog/overview.html', context)

def article_detail(request, pk):
    context = {
        'title': 'Blog',
        'article': Article.objects.get(id = pk),
        'comments': Article.objects.get(id = pk).comment_set.all(),
        'form': CommentForm,
    }
    return render(request, 'blog/article.html', context)

class CreateCommentView(View):
    template_name = 'blog/article.html'

    def post(self, request, *args, **kwargs):
        article_id = self.request.POST.get('article_id')
        comment = self.request.POST.get('comment')

        article = Article.objects.get(id = article_id)
        new_comment = article.comment_set.create(author = request.user, content = comment)
        comment = [
            {'author':new_comment.author.username,
             'comment': new_comment.content,
             'timestemp':new_comment.timestemp.strftime('%d/%m/%Y'),
             }
        ]
        return JsonResponse(comment, safe = False)
