import json
from catalog.models import Product, Category
from django.core.management import BaseCommand


class Command(BaseCommand):
    @staticmethod
    def json_read_categories():
        with open('data/catalog_data.json', "r", encoding="utf-8") as f:
            json_file = json.load(f)
            categories_list = []
            for i in json_file:
                if i["model"] == "catalog.category":
                    categories_list.append(i)
            return categories_list

    @staticmethod
    def json_read_products():
        with open('data/catalog_data.json', "r", encoding="utf-8") as f:
            json_file = json.load(f)
            products_list = []
            for i in json_file:
                if i["model"] == "catalog.product":
                    products_list.append(i)
            return products_list

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        product_for_create = []
        category_for_create = []

        for category in Command.json_read_categories():
            category_for_create.append(
                category(id=category["pk"], name=category["fields"]["name"],
                         description=category["fields"]["description"])
            )

        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products():
            product_for_create.append(
                product(id=product["pk"], name=product["fields"]["name"], description=product["fields"]["description"],
                        photo=product["fields"]["photo"], category=Category.objects.get(pk=product["fields"]["pk"]),
                        price=product["fields"]["price"], created_at=product["fields"]["created_at"],
                        updated_at=product["fields"]["updated_at"])
            )

        Product.objects.bulk_create(product_for_create)
