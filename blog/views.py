from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Article, Tag


def index(request):
    articles = Article.objects.get_queryset()
    return render(request, 'blog/index.html', {'articles': articles})


def get_article(request, slug: str):
    article = get_object_or_404(Article, slug=slug)
    tags = article.tags.get_queryset()
    return render(request, 'blog/single.html', {'article': article, 'tags': tags})
