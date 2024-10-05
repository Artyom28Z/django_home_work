from django.contrib import admin
from articles.models import Article


# Register your models here.


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "is_active", "created_at", "view_counter")
    list_filter = ("id", "is_active", "title", "created_at", "view_counter")
    search_fields = ("title", "content",)

