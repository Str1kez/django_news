from django import template

from blog.models import Tag
import datetime as dt

register = template.Library()


@register.simple_tag
def get_tags(count: int=20):
    return Tag.objects.get_queryset()[:count]


@register.simple_tag()
def get_date():
    return dt.date.today()
