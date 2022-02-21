from django import template
from django.db.models import Count

from blog.models import Tag, Article
import datetime as dt

register = template.Library()


@register.simple_tag
def article_tags(count: int = 20):
    return Tag.objects.annotate(article_count=Count('tags__id')).filter(article_count__gt=0)[:count]


@register.simple_tag
def header_date():
    return dt.date.today()


@register.simple_tag
def popular_posts(count: int = 5):
    return Article.objects.order_by('-views')[:count]
