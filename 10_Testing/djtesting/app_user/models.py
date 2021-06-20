from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('Пользователь'))
    city = models.CharField(_('Город'), max_length=20, blank=True)
    telephone = models.CharField(_('Телефон'), max_length=20, blank=False)
    avatar = models.ImageField(_('Аватарка'), upload_to='avatars/', blank=True, null=True)

    class Meta:
        verbose_name = _("Модель пользователя")
        verbose_name_plural = _("Модель пользователей")
