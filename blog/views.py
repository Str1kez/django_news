from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

# Create your views here.
from .models import Article, Tag


def index(request):
    articles = Article.objects.get_queryset()
    paginator = Paginator(articles, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/index.html', {'page_obj': page_obj})


def get_article(request, slug: str):
    article = get_object_or_404(Article, slug=slug)
    article.views += 1
    article.save()
    
    tags = article.tags.get_queryset()
    return render(request, 'blog/single.html', {'article': article, 'tags': tags})


def get_articles_by_tag(request, slug: str):
    tag = get_object_or_404(Tag, slug=slug)
    articles = tag.tags.get_queryset()
    paginator = Paginator(articles, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/index.html', {'page_obj': page_obj, 'title': tag.title})
