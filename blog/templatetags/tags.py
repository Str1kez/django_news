from django import template
from django.db.models import Count
from django.contrib.auth.models import User
from django.core.cache import cache

from blog.models import Tag, Article
import datetime as dt

register = template.Library()


@register.simple_tag
def article_tags():
    tags = cache.get('tags')
    if not tags:
        cache.set('tags', Tag.objects.annotate(article_count=Count('tags__id')).filter(article_count__gt=0)[:20])
        return cache.get('tags')
    return tags


@register.simple_tag
def header_date():
    return dt.date.today()


@register.simple_tag
def popular_posts():
    posts = cache.get('posts')
    if not posts:
        cache.set('posts', Article.objects.order_by('-views')[:5])
        return cache.get('posts')
    return posts


@register.simple_tag
def popular_users():
    return User.objects.annotate(article_count=Count('article')).filter(article_count__gt=0)\
                    .order_by('-article_count')[:10]

