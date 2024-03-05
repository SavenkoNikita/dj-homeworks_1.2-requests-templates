import csv
from pprint import pprint

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        try:
            with open('phones.csv', 'r') as file:
                phones = list(csv.DictReader(file, delimiter=';'))

            for phone in phones:
                if Phone.objects.filter(id=phone['id'], name=phone['name']).exists() is False:
                    print(f'Добавлены новые данные:\n'
                          f'id = {phone["id"]}\n'
                          f'name = {phone["name"]}\n'
                          f'image = {phone["image"]}\n'
                          f'price = {phone["price"]}\n'
                          f'release_date = {phone["release_date"]}\n'
                          f'lte_exists = {phone["lte_exists"]}\n')
                    # TODO: Добавьте сохранение модели
                    Phone.objects.create(
                        id=phone['id'],
                        name=phone['name'],
                        image=phone['image'],
                        price=phone['price'],
                        release_date=phone['release_date'],
                        lte_exists=phone['lte_exists']
                    )
        except Exception as error:
            print(f'При создании нового значения в БД возникло исключение:\n!!!\n{error}!!!\n')
            pass
