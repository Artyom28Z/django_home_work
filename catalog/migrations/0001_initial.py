# Generated by Django 5.1.1 on 2024-09-26 14:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название категории', max_length=50, verbose_name='Название категории')),
                ('description', models.TextField(blank=True, help_text='Введите описание категории', null=True, verbose_name='Описание категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название продукта', max_length=50, verbose_name='Название продукта')),
                ('description', models.TextField(blank=True, help_text='Введите описание продукта', null=True, verbose_name='Описание продукта')),
                ('photo', models.ImageField(blank=True, help_text='Загрузите фото продукта', null=True, upload_to='catalog/photo', verbose_name='Фото')),
                ('price', models.IntegerField(help_text='Введите цену', verbose_name='Цена за покупку')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания продукта в базе данных')),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата последнего изменения продукта в БД')),
                ('category', models.ForeignKey(blank=True, help_text='Введите категорию продукта', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='catalog', to='catalog.category', verbose_name='Категория продукта')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ['name', 'category', 'price', 'created_at'],
            },
        ),
    ]
