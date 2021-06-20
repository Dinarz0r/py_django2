from django.db import models


class AdvertisementUser(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, db_index=True, verbose_name='Имя')
    email = models.EmailField(verbose_name='Электронная почта', )
    number_phones = models.IntegerField(verbose_name='Телефон')

    class Meta:
        db_table = 'User'

    def __str__(self):
        return self.name


class Advertisement(models.Model):
    title = models.CharField(max_length=1000, db_index=True, verbose_name='Заголовок')
    description = models.TextField(max_length=1000, default='', verbose_name='Описание', db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    when_to_stop_at = models.DateTimeField(default=None, null=True, blank=True,
                                           verbose_name='дата окончания публикации')
    update_at = models.DateTimeField(auto_now=True)
    price = models.FloatField(verbose_name='Цена', default=0)
    view_count = models.IntegerField(verbose_name='Количество просмотров', default=0)
    status = models.ForeignKey('AdvertisementStatus', default=None, null=True, on_delete=models.CASCADE,
                               related_name='advertisements', verbose_name='Статус')
    user = models.ForeignKey('AdvertisementUser', blank=False, on_delete=models.CASCADE, verbose_name='Пользователь',
                             related_name='advertisements', null=True, default=None)
    categories = models.ForeignKey("AdvertisementCategories", default=None, null=True, on_delete=models.CASCADE,
                                   related_name='advertisements', verbose_name='Наименование')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Advertisements'
        ordering = ['title']


class AdvertisementStatus(models.Model):
    name = models.CharField(max_length=100, verbose_name='Cтатус')

    def __str__(self):
        return self.name


class AdvertisementCategories(models.Model):
    adcategories = models.CharField(max_length=100, verbose_name='Наименование')

    class Meta:
        db_table = 'Categories'

    def __str__(self):
        return self.adcategories
