from django.core.management.base import BaseCommand
from catalog.models import Product, Category

class Command(BaseCommand):
    help = 'заполнения базы-данных о продуктах'

    def handle(self, *args, **options):
        # Удаляем существующие записи
        Product.objects.all().delete()

        category, _ = Category.objects.get_or_create(name='бакалея', description='Разные сыпучие продукты')

        products = [
            {'name': 'рис', 'description': 'бурый', 'category': category, 'price': '123,14'},
            {'name': 'гречка', 'description': 'зеленая', 'category': category, 'price': '83,14'}
        ]

        for prod in products:
            product, created = Product.objects.get_or_create(**prod)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: '
                                                     f'{product.name} {product.description}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exists: '
                                                     f'{product.name} {product.description}'))
