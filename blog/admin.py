from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from blog.models import Article, Tag


class ArticleAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'author', 'created_at', 'get_image'
    list_display_links = 'id', 'title'
    list_editable = 'author',
    list_filter = 'author', 'created_at'
    search_fields = 'title', 'author', 'created_at'
    actions_on_top = True
    ordering = '-created_at', 'title'

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" alt="Не загрузилась" width=75>')

    get_image.short_description = 'Картинка'


admin.site.register(Tag)
admin.site.register(Article, ArticleAdmin)
