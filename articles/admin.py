from django.contrib import admin
from articles.models import Article


# Register your models here.


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "is_active", "created_at", "view_counter", "slug")
    list_filter = ("is_active", "title", "created_at", "view_counter")
    search_fields = ("title", "content", "slug")
    prepopulated_fields = {"slug": ("title",)}
