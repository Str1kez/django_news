from django.urls import path

from blog.views import index, get_article

app_name = 'blog'

urlpatterns = [
    path('', index, name='home'),
    path('article/<str:slug>', get_article, name='get_article')
]
