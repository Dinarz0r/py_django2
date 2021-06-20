from django.db import models


class ItemModel(models.Model):
    """Модель товара"""
    name = models.CharField('Название', max_length=30)
    description = models.TextField('Описание', max_length=1000, blank=True)
    weight = models.FloatField('Вес')
