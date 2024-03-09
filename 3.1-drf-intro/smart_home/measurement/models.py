from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=80, verbose_name='Название датчика')
    description = models.TextField(verbose_name='Описание')


class Measurement(models.Model):
    temperature = models.FloatField(verbose_name='Температура')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    id_sensor = models.ForeignKey(Sensor,
                                  related_name='measurements',
                                  on_delete=models.CASCADE,
                                  verbose_name='№ датчика')
