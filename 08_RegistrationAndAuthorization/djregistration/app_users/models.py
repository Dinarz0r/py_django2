from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    VERIFICATION_CHOICE = [
        ('u', 'Обычный пользователь'),
        ('v', 'Верифицированный пользователь'),
        ('m', 'Модератор'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telephone = models.CharField('Телефон', max_length=30, blank=True)
    city = models.CharField('Город', max_length=30, blank=True)
    verification = models.CharField('Флаг верификации', max_length=1, default='u', blank=True,
                                    choices=VERIFICATION_CHOICE)
    count_published_news = models.IntegerField("Количество опубликованных новостей", default=0, blank=True)

    class Meta:
        verbose_name = "Аккаунт(ы)"
        verbose_name_plural = "Профиль"

    def __str__(self):
        return self.user.username
