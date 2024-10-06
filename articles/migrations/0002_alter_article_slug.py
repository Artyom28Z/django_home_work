# Generated by Django 5.1.1 on 2024-10-05 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="slug",
            field=models.SlugField(max_length=255, unique=True, verbose_name="URL"),
        ),
    ]
