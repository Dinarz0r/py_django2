from django.db import models


class Vacancy(models.Model):
    is_active = models.BooleanField('Активность', default=False)
    title = models.CharField('Заголовок', max_length=30)
    description = models.TextField('Описание', default='')
    publisher = models.CharField('Кто опубликовал', max_length=30)
    create_at = models.DateTimeField('Дата создания', auto_now_add=True)
    published_at = models.DateTimeField('Дата публикации', blank=True, null=True)

    class Meta:
        verbose_name = 'вакансия'
        verbose_name_plural = 'вакансии'
        permissions = (
            ('can_publish', "Может публиковать"),
        )

    def __str__(self):
        return self.title


class Summary(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    create_at = models.DateTimeField('Дата создания', auto_now_add=True)
    published_at = models.DateTimeField('Дата публикации', blank=True, null=True)
    description = models.TextField('Описание', default='')

    class Meta:
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'
        # permissions = (
        #     ('can_publish', "Может публиковать"),
        # )
