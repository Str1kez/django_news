from django import template

from blog.models import Tag, Article
import datetime as dt

register = template.Library()


@register.simple_tag
def article_tags(count: int = 20):
    return Tag.objects.get_queryset()[:count]


@register.simple_tag
def header_date():
    return dt.date.today()


@register.simple_tag
def popular_posts(count: int = 5):
    return Article.objects.order_by('-views')[:count]
