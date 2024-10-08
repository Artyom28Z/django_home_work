from django.urls import path
from articles.apps import CatalogConfig
from articles.views import (
    contacts,
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView,
)

app_name = CatalogConfig.name


urlpatterns = [
    path("", ArticleListView.as_view(), name="article_list"),
    path("<slug:slug>/", ArticleDetailView.as_view(), name="article_detail"),
    path("create_article", ArticleCreateView.as_view(), name="article_create"),
    path("<slug:slug>/update/", ArticleUpdateView.as_view(), name="article_update"),
    path("<slug:slug>/delete/", ArticleDeleteView.as_view(), name="article_delete"),
    path("contacts/", contacts, name="contacts"),
]
