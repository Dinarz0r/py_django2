from django.db import models


class ItemGroupModel(models.Model):
    group_name = models.CharField(max_length=70, verbose_name='Группа товаров')

    def __str__(self):
        return f'{self.id} - {self.group_name}'


class Item(models.Model):
    name = models.CharField('Название', max_length=200)
    description = models.TextField('Описание', blank=True)
    weight = models.FloatField(verbose_name='Вес')
    group_name = models.ManyToManyField(ItemGroupModel, verbose_name='Группа товара', blank=True,
                                        related_name='test', related_query_name='name1')
