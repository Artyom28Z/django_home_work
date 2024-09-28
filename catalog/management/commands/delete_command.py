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
                for k, v in json_file.items():
                    if v == "catalog.category":
                        categories_list.append(i)
            return categories_list

    @staticmethod
    def json_read_products():
        with open('data/catalog_data.json', "r", encoding="utf-8") as f:
            json_file = json.load(f)
            products_list = []
            for i in json_file:
                for k, v in json_file.items():
                    if v == "catalog.product":
                        products_list.append(i)
            return products_list

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        product_for_create = []
        category_for_create = []

        for category in Command.json_read_categories():
            category_for_create.append(
                category(id="pk", name="fields"["name"], description="fields"["description"])
            )

        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products():
            product_for_create.append(
                product(id="pk", name="fields"["name"], description="fields"["description"], photo="fields"["photo"],
                        category=Category.objects.get(pk="fields"["pk"]), price="fields"["price"],
                        created_at="fields"["created_at"], updated_at="fields"["updated_at"])
            )

        Product.objects.bulk_create(product_for_create)
