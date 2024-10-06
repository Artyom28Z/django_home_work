from unidecode import unidecode
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from articles.models import Article


# Create your views here.


class ArticleListView(ListView):
    model = Article


class ArticleDetailView(DetailView):
    model = Article

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        self.object.save()
        return self.object


class ArticleCreateView(CreateView):
    model = Article
    fields = ("title", "content", "photo", "is_active")
    success_url = reverse_lazy("articles:article_list")

    def form_valid(self, form):
        form.instance.slug = slugify(unidecode(form.instance.title))
        return super().form_valid(form)


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ("title", "content", "photo", "is_active")
    success_url = reverse_lazy("articles:article_list")

    def get_success_url(self):
        return reverse("articles:article_detail", kwargs=[self.kwargs.get("slug")])


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy("articles:article_list")


def contacts(request):
    return render(request, "articles/contacts.html")
