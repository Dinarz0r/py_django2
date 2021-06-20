from django.db import models
from random import randint


class AuthorModel(models.Model):
    """Модель Автора"""
    name = models.CharField('Имя', max_length=30)
    surname = models.CharField('Фамилия', max_length=30)
    date_bd = models.DateField('Дата рождения')

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = "Авторы"

    def __str__(self):
        return f'{self.surname} {self.name}'


class BookModel(models.Model):
    """Модель книги"""
    title = models.CharField('Название', max_length=200)
    date_release = models.IntegerField('Год выпуска')
    isbn = models.IntegerField(default=randint(100000000, 999999999))
    count_pages = models.IntegerField('Количество листов')
    author = models.ForeignKey(AuthorModel, verbose_name="Автор", on_delete=models.CASCADE, blank=False, null=False,
                               related_name='author')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = "Книги"
