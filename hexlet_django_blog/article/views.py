from django.shortcuts import render
from django.views import View
from hexlet_django_blog.article.models import Article

def index(request, tags, article_id):
    return render(request, 'article.html', context={'tags': tags, 'article_id': article_id})


class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:3]
        return render(request, 'articles/article.html', context={
            'articles': articles,
        })