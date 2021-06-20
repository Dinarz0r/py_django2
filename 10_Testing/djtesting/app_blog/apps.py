from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MyBlogConfig(AppConfig):
    name = 'app_blog'
    verbose_name = _('Блог')
