from django import template

from blog.models import Tag

register = template.Library()


@register.simple_tag
def get_tags():
    return Tag.objects.get_queryset()
