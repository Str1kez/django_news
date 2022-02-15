import datetime

from django import template

from blog.models import Tag
import datetime as dt

register = template.Library()


@register.simple_tag
def get_tags():
    return Tag.objects.get_queryset()


@register.simple_tag()
def get_date():
    return dt.date.today()
