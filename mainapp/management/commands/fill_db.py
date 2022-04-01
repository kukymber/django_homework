import json
from django.core.management.base import BaseCommand

from authapp.models import User
from mainapp.models import ProductCategory, Product


def load_from_json(file_name):
    with open(file_name, mode='r', encoding='utf-8') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        User.objects.create_superuser(username='Anatolii', email='mail@mail.ru', password='1')
        category = load_from_json('C:/Users/ElenaOstapenko/PycharmProjects/django/django_homework/mainapp/fixtures/category.json')

        ProductCategory.objects.all().delite()
        for categor in category:
            cat = categor.get('fields')
            cat['id'] = categor.get('pk')
            new_category = ProductCategory(**cat)
            new_category.save()

        products = load_from_json('C:/Users/ElenaOstapenko/PycharmProjects/django/django_homework/mainapp/fixtures/product.json')

        Product.objects.all().delite()
        for product in products:
            prod = product.get('fields')
            category = prod.get('category')
            _category = ProductCategory.objects.get(id=category)
            prod['category'] = _category
            new_category = Product(**prod)
            new_category.save()
