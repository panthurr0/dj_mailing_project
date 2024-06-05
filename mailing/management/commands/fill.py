import json
import pathlib

from django.core.management import BaseCommand
from django.db import connection

from blog.models import Blog
from catalog.models import Category, Product, Version
from users.models import User

ROOT = pathlib.Path(__file__).parent.parent.parent.parent
DATA_CLIENT = pathlib.Path(ROOT, 'json_data', 'client.json')
DATA_MAILINGTEXT = pathlib.Path(ROOT, 'json_data', 'mailingtext.json')
DATA_MAILING = pathlib.Path(ROOT, 'json_data', 'mailing.json')
DATA_STATUS = pathlib.Path(ROOT, 'json_data', 'status.json')
DATA_MAILING = pathlib.Path(ROOT, 'json_data', 'mailing.json')
DATA_MAILING = pathlib.Path(ROOT, 'json_data', 'mailing.json')



class Command(BaseCommand):

    @staticmethod
    def json_read(path) -> list:
        # Здесь мы получаем данные из фикстур
        with open(path) as file:
            file_info = json.load(file)
        return [info for info in file_info]

    def handle(self, *args, **options):
        # Очистка базы данных перед заполнением
        Category.objects.all().delete()
        Product.objects.all().delete()
        Version.objects.all().delete()
        Blog.objects.all().delete()

        category_for_create = []
        product_for_create = []
        version_for_create = []
        blog_for_create = []

        with connection.cursor() as cursor:
            cursor.execute(
                "TRUNCATE TABLE catalog_category, catalog_product, catalog_version, "
                "blog_blog RESTART IDENTITY CASCADE;")

        # Заполнение категорий
        for category in Command.json_read(DATA_CATEGORY):
            category_fields = category.get('fields')
            category_for_create.append(
                Category(category_title=category_fields.get('category_title'),
                         category_description=category_fields.get('category_description'))
            )

        Category.objects.bulk_create(category_for_create)

        # Заполнение продуктов
        for product in Command.json_read(DATA_PRODUCT):
            product_fields = product.get('fields')
            product_for_create.append(
                Product(product_title=product_fields.get('product_title'),
                        category=Category.objects.get(pk=product_fields.get('category')),
                        price=product_fields.get('price'),
                        owner=User.objects.get(pk=product_fields.get('owner')),
                        is_active=product_fields.get('is_active'),
                        product_description=product_fields.get('product_description'),
                        image=product_fields.get('image'))
            )
        Product.objects.bulk_create(product_for_create)

        # Заполнение версий
        for version in Command.json_read(DATA_VERSIONS):
            version_fields = version.get('fields')
            version_for_create.append(
                Version(product=Product.objects.get(pk=version_fields.get('product')),
                        version_number=version_fields.get('version_number'),
                        version_title=version_fields.get('version_title'),
                        is_active=version_fields.get('is_active'))
            )
        Version.objects.bulk_create(version_for_create)

        # Заполнение блогов
        for blog in Command.json_read(DATA_BLOG):
            blog_fields = blog.get('fields')
            blog_for_create.append(
                Blog(title=blog_fields.get('title'),
                     content=blog_fields.get('content'),
                     preview=blog_fields.get('preview'),
                     is_published=blog_fields.get('is_published'))
            )
        Blog.objects.bulk_create(blog_for_create)
