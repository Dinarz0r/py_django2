from django.contrib.auth.models import User
from django.db import models
from app_user.models import UserModel


class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField('Заголовок', max_length=100)
    text = models.TextField('Текст статьи', max_length=3000)
    create_at = models.DateTimeField('Дата создания новости', auto_now_add=True)
    update_at = models.DateTimeField('Дата обновления статьи', auto_now=True)
    publication_date = models.DateTimeField("Дата публикации", null=True, blank=True)
    publish_flag = models.BooleanField(verbose_name='Опубликовать блог', default=True)

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = "Блоги"
        ordering = ['-create_at']
        permissions = (
            ('can_publish', "Может публиковать"),
        )

    def get_text_100(self):
        if len(self.text) > 100:
            return self.text[:101] + '...'
        return self.text

    def __str__(self):
        return f'{self.user}: {self.get_text_100()}'


class ImagesModel(models.Model):
    image = models.ImageField('Изображение', upload_to='image/', blank=True, null=True)
    blog = models.ForeignKey(Blog,
                             verbose_name='Блог',
                             on_delete=models.CASCADE)
