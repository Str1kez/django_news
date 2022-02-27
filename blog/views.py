from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from random import randint

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import ArticleForm
from .models import Article, Tag


class CreateArticle(LoginRequiredMixin, CreateView):
    form_class = ArticleForm
    template_name = 'blog/create.html'
    permission_denied_message = 'Авторизуйтесь'
    login_url = reverse_lazy('user:sign_in')

    def form_valid(self, form):
        """Добавляем юзера, который пишет данную статью"""
        form.instance.user = self.request.user
        return super().form_valid(form)


def index(request):
    articles = Article.objects.get_queryset()

    paginator = Paginator(articles, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/index.html', {'page_obj': page_obj})


def get_article(request, slug: str = None, article: Article = None):
    if not article:
        article = get_object_or_404(Article, slug=slug)
    article.views += 1
    article.save()
    
    tags = article.tags.all()
    return render(request, 'blog/single.html', {'article': article, 'tags': tags})


def get_articles_by_tag(request, slug: str):
    tag = get_object_or_404(Tag, slug=slug)
    articles = tag.tags.all()

    paginator = Paginator(articles, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/index.html', {'page_obj': page_obj, 'title': tag.title})


def get_articles_by_user(request, username: str):
    articles = Article.objects.filter(user__username=username)

    paginator = Paginator(articles, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/index.html', {'page_obj': page_obj, 'title': username})


def get_random_article(request):
    count = Article.objects.count()
    id = randint(1, count)
    article = get_object_or_404(Article, id=id)
    return get_article(request, article=article)
    # return redirect('blog:get_article', article.slug)


def get_results(request):
    query = request.GET.get('s')
    if query:
        articles = Article.objects.filter(title__icontains=query)

        paginator = Paginator(articles, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'blog/search.html', {'page_obj': page_obj, 'query': query})
    return render(request, 'blog/search.html')
