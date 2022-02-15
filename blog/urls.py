from django.urls import path

from blog.views import index, get_article, get_articles_by_tag

app_name = 'blog'

urlpatterns = [
    path('', index, name='home'),
    path('article/<str:slug>', get_article, name='get_article'),
    path('tag/<str:slug>', get_articles_by_tag, name='get_articles_by_tag'),
]
