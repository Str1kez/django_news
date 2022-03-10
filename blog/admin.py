from django.contrib import admin

# Register your models here.
from django import forms
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from blog.models import Article, Tag


class ArticleAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Article
        fields = '__all__'


class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm

    list_display = 'id', 'title', 'slug', 'author', 'user', 'created_at', 'views', 'get_image'
    list_display_links = 'id', 'title'
    list_editable = 'author',
    list_filter = 'author', 'created_at', 'user'
    search_fields = 'title', 'author', 'created_at'
    ordering = '-created_at', '-views'
    actions_on_top = True

    fields = 'title', 'slug', 'author', 'content', 'image', 'get_image', 'tags', 'views', 'created_at', 'user'
    readonly_fields = 'get_image', 'created_at', 'views'
    prepopulated_fields = {'slug': ('title',)}

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" alt="Не загрузилась" width=75>')

    get_image.short_description = 'Картинка'


class TagAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'slug'
    list_display_links = 'id', 'title'
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(Tag, TagAdmin)
admin.site.register(Article, ArticleAdmin)
