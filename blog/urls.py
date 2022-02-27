from django.urls import path

from .views import index, get_article, get_articles_by_tag, \
                    get_results, get_random_article, get_articles_by_user, CreateArticle

app_name = 'blog'

urlpatterns = [
    path('', index, name='home'),
    path('creator/<str:username>', get_articles_by_user, name='get_articles_by_user'),
    path('new_article/', CreateArticle.as_view(), name='create_article'),
    path('article/<str:slug>', get_article, name='get_article'),
    path('random/', get_random_article, name='random_article'),
    path('search/', get_results, name='search'),
    path('tag/<str:slug>', get_articles_by_tag, name='get_articles_by_tag'),
]
