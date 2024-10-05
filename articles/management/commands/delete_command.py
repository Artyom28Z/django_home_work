import json
from articles import Article
from django.core.management import BaseCommand


class Command(BaseCommand):
    @staticmethod
    def json_read_articles():
        with open('data/catalog_data.json', "r", encoding="utf-8") as f:
            json_file = json.load(f)
            article_list = []
            for i in json_file:
                if i["model"] == "articles_.article":
                    article_list.append(i)
            return article_list

    def handle(self, *args, **options):
        Article.objects.all().delete()

        article_for_create = []

        for article in Command.json_read_articles():
            article_for_create.append(
                Article(id=article["pk"], title=article["fields"]["title"],
                        content=article["fields"]["content"],
                        updated_at=article["fields"]["updated_at"],
                        photo=article["fields"]["photo"],
                        is_active=article["fields"]["is_active"],
                        slug=article["fields"]["slug"])
            )

        Article.objects.bulk_create(article_for_create)
