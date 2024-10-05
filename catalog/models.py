from django.db import models
# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название категории', help_text='Введите название категории')
    description = models.TextField(verbose_name='Описание категории', help_text='Введите описание категории',
                                   **NULLABLE)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название продукта', help_text='Введите название продукта')
    description = models.TextField(verbose_name='Описание продукта', help_text='Введите описание продукта',
                                   **NULLABLE)
    photo = models.ImageField(upload_to='catalog/photo', verbose_name='Фото', help_text='Загрузите фото продукта',
                              **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name='Категория продукта',
                                 help_text='Выберите категорию продукта', related_name='products', **NULLABLE)
    price = models.IntegerField(verbose_name='Цена за покупку', help_text='Введите цену')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания продукта в базе данных')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата последнего изменения продукта в БД',
                                      **NULLABLE)
    view_counter = models.PositiveIntegerField(verbose_name='Счётчик просмотров', help_text='Подсчёт просмотров',
                                               default=0)
    is_active = models.BooleanField(verbose_name='Наличие в продаже', help_text='Укажите есть ли на складе',
                                    default=True)
    #manufactured_at = models.DateField(verbose_name='Дата производства продукта',
                                           #help_text='Введите дату производства продукта', **NULLABLE)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name', 'category', 'price', 'created_at']

    def __str__(self):
        return self.name
