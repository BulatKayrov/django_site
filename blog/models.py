import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

User = get_user_model()


class Category(models.Model):
    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    title = models.CharField(max_length=100, unique=True, verbose_name='Название категории')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='Ссылка')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(viewname='blog:category_filter', kwargs={'category_slug': self.slug})


class Post(models.Model):
    PUBLISHED = "PUBLISHED"
    DRAFT = "DRAFT"
    IS_PUBLISHED = [(PUBLISHED, "PUBLISHED"), (DRAFT, "DRAFT")]
    MAX_LENGTH = len(PUBLISHED)

    class Meta:
        verbose_name = 'Статью'
        verbose_name_plural = 'Статьи'

    title = models.CharField(max_length=100, unique=True, verbose_name='Название статьи')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='Ссылка')
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name='posts', verbose_name='Категория')
    content = models.TextField(default='Здесь будет контент ...', verbose_name='Текст статьи')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(verbose_name='Дата изменения', blank=True, null=True)
    is_published = models.CharField(max_length=MAX_LENGTH, choices=IS_PUBLISHED, default=DRAFT, verbose_name='Статус')
    image = models.ImageField(upload_to='post/', blank=True, null=True, verbose_name='Изображение')
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='posts', verbose_name='Автор')
    count_views = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(viewname='blog:post_detail', kwargs={'post_slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title) + f'_{uuid.uuid4().hex}'
        return super().save(*args, **kwargs)

    def get_image_url(self):
        if self.image:
            return self.image.url
        return 'https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__340.jpg'

    def get_image_thumbnail(self):
        if self.image:
            return self.image.url
