from django.core.management import BaseCommand
import json
from catalog.models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open('catalog_data.json', encoding='UTF-16') as file:
            data = json.load(file)
            return data

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        category_for_create = []

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            category_for_create.append(
                Category(**category['fields'])
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

        product_for_create = [
            {'name': 'gel', 'description': 'just text', 'image': '', 'category': category_for_create[2], 'price': '200', 'created_at': '2022-01-10', 'updated_at': '2022-01-17'},
            {'name': 'powder', 'description': 'text', 'image': '', 'category': category_for_create[2], 'price': '1000', 'created_at': '2022-06-11', 'updated_at': '2022-06-12'},
            {'name': 'shampoo', 'description': 'for head', 'image': '', 'category': category_for_create[2], 'price': '500', 'created_at': '2022-08-09', 'updated_at': '2022-08-10'}
        ]

        for products_item in product_for_create:
            Product.objects.create(**products_item)
