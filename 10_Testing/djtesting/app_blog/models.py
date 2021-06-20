from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Автор'))
    title = models.CharField(_('Заголовок'), max_length=100)
    text = models.TextField(_('Текст статьи'), max_length=3000)
    create_at = models.DateTimeField(_('Дата создания блога'), auto_now_add=True)
    update_at = models.DateTimeField(_('Дата обновления статьи'), auto_now=True)
    publication_date = models.DateTimeField(_("Дата публикации"), null=True, blank=True)
    publish_flag = models.BooleanField(_('Опубликовать блог'), default=True)

    class Meta:
        verbose_name = _('Блог')
        verbose_name_plural = _("Блоги")
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
    image = models.ImageField(_('Изображение'), upload_to='image/', blank=True, null=True)
    blog = models.ForeignKey(Blog,
                             verbose_name=_('Блог'),
                             on_delete=models.CASCADE)
