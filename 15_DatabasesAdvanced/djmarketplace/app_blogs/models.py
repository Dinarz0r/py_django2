from django.contrib.auth.models import User
from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=200)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'

    def __str__(self):
        return self.name


class Moderator(models.Model):
    name = models.CharField('имя модератора', max_length=100)

    class Meta:
        verbose_name = 'модератор'
        verbose_name_plural = 'модераторы'

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField('имя автора', max_length=100)

    class Meta:
        verbose_name = 'автор'
        verbose_name_plural = 'авторы'

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    text = models.TextField('текст поста')
    create_at = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, db_index=True, related_name='posts')
    author = models.ManyToManyField(Author, related_name='posts')
    moderator = models.ForeignKey(Moderator, on_delete=models.CASCADE, blank=True, null=True)
    likes_count = models.PositiveIntegerField('Лайки', default=0)

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'

    def __str__(self):
        return self.title


class Profile(models.Model):
    VERIFICATION_CHOICE = [
        ('newbie', 'Новичок'),
        ('Advanced', 'Продвинутый'),
        ('Expert', 'Эксперт'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    verification = models.CharField('Флаг верификации', max_length=10, default='newbie', blank=False,
                                    choices=VERIFICATION_CHOICE)
    points_status = models.IntegerField('баллы', default=500)

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Аккаунт(ы)"

    def __str__(self):
        return self.user.username
