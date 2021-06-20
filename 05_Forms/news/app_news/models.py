from django.contrib.auth.models import User
from django.db import models


class News(models.Model):
    """
    Модель БД новостей
    Attributes:
        id = идентификационный номер новости
        title = Заголовок новости
        description str = Текст новости
        create_at = дата создания новости
        update_at = дата обновления новости
        activity_flag = флаг активности
    """
    user = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField('Название', max_length=200)
    text = models.TextField('Текст статьи')
    create_at = models.DateTimeField('Дата публикации', auto_now_add=True)
    update_at = models.DateTimeField('Дата обновления статьи', auto_now=True)
    activity_flag = models.BooleanField(verbose_name='Активность', default=True)

    class Meta:
        verbose_name_plural = "Новости"
        ordering = ['-create_at']

    def __str__(self):
        return f'{self.create_at}-{self.title}'


class Comments(models.Model):
    """
    Класс Модели комментариев к новостной ленте.
    Attributes:
         user = имя комментатора
         comment = текст комментария
         news = отношение к классу модели NewsModel
    """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь', blank=True, null=True)

    username = models.CharField('Имя', max_length=20)
    new = models.ForeignKey(News,
                            verbose_name='Новость',
                            on_delete=models.CASCADE)
    text = models.TextField("Комментарий", max_length=500)
    create_at = models.DateTimeField("Дата добавления", auto_now_add=True, null=True)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def get_comment(self):
        comment = self.text
        if len(comment) > 15:
            comment = comment[:15] + '...'
        return comment

    def __str__(self):
        return self.user
