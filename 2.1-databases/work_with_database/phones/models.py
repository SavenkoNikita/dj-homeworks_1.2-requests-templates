from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(),
    price = models.CharField(),
    image = models.CharField(),
    release_date = models.DateField(),
    lte_exists = models.CharField()
