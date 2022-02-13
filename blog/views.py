from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Article


def index(request):
    return render(request, 'blog/index.html')


def get_article(request, slug: str):
    article = get_object_or_404(Article, slug=slug)
    print(article.tags)
    return render(request, 'blog/single.html', {'article': article})
