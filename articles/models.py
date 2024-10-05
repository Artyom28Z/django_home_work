from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок', help_text='Введите заголовок статьи')
    content = models.TextField(verbose_name='Статья', help_text='Введите текст статьи')
    photo = models.ImageField(upload_to='articles_/photo', verbose_name='Фото', help_text='Загрузите фото для статьи',
                              **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания статьи в базе данных')

    view_counter = models.PositiveIntegerField(verbose_name='Счётчик просмотров', help_text='Подсчёт просмотров',
                                               default=0)
    is_active = models.BooleanField(verbose_name='Опубликовано', help_text='Укажите опубликовать или нет',
                                    default=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['title', 'created_at', 'view_counter']

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})



