from django.db import models

# Create your models here.
from django.urls import reverse
from django.contrib.auth.models import User

from uuslug import uuslug


class Tag(models.Model):
    title = models.CharField(max_length=50, blank=False, verbose_name='Название')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:get_articles_by_tag', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'


class Article(models.Model):
    title = models.CharField(max_length=255, blank=False, verbose_name='Заголовок')
    content = models.TextField(blank=False, verbose_name='Текст')
    image = models.ImageField(upload_to='images/%Y/%m/%d/', verbose_name='Изображение', blank=True)
    views = models.IntegerField(verbose_name='Просмотры', default=0)
    author = models.CharField(max_length=255, blank=False, verbose_name='Автор')
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=False, max_length=50, verbose_name='Url', unique=True)
    tags = models.ManyToManyField(Tag, 'tags')
    user = models.ForeignKey(User, on_delete=models.SET('Unknown'), verbose_name='Пользователь', default=1)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:get_article', kwargs={'slug': self.slug})

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        update_fields = kwargs.get('update_fields')
        if update_fields is None or len(update_fields) != 1 or 'views' not in update_fields:
            self.slug = uuslug(self.title, instance=self, max_length=50)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = '-created_at',
