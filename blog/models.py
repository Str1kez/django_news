from django.db import models

# Create your models here.
from django.urls import reverse


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
    slug = models.SlugField(max_length=50, verbose_name='Url', unique=True)
    tags = models.ManyToManyField(Tag, 'tags')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:get_article', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = '-created_at',
