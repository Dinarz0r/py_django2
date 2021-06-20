from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AppUserConfig(AppConfig):
    name = 'app_user'
    verbose_name = _('Модель пользователя')
    verbose_name_plural = _('Модель пользователей')
