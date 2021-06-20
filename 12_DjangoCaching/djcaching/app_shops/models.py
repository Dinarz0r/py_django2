import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

A_WEEK = datetime.datetime.now().date() + datetime.timedelta(days=7)


class ShopsModel(models.Model):
    name_shop = models.CharField(_('Название магазина'), max_length=30)
    telephone = models.CharField(_('Телефон магазина'), max_length=30)

    def __str__(self):
        return self.name_shop


class ProductsModel(models.Model):
    product = models.CharField(_('Товар'), max_length=30)
    price = models.DecimalField(_('Цена'), max_digits=10, decimal_places=2)
    article = models.AutoField(_('Артикул'), primary_key=True)
    shop = models.ForeignKey(ShopsModel, verbose_name=_('Магазин'), on_delete=models.CASCADE, related_name='shop')

    def __str__(self):
        return self.product


class PurchaseHistoryModel(models.Model):
    user = models.ForeignKey(User, verbose_name=_('Имя покупателя'), on_delete=models.CASCADE, related_name='user')
    goods = models.ForeignKey(ProductsModel, verbose_name=_('Товар'),
                              on_delete=models.CASCADE, related_name='goods')
    price = models.DecimalField(_('Цена покупки'), max_digits=10, decimal_places=2)
    purchase_date = models.DateTimeField(_('Дата покупки'), auto_now_add=True)


class PromotionsModel(models.Model):
    promotion = models.CharField(_('Акция'), max_length=100)
    validity_period = models.DateField(default=A_WEEK, null=True)

    class Meta:
        verbose_name = _("Акция")
        verbose_name_plural = _("Акции")


class OffersModel(models.Model):
    offer = models.CharField(_('Предложение'), max_length=500)
    validity_period = models.DateField(default=A_WEEK, null=True)

    class Meta:
        verbose_name = _("Предложение")
        verbose_name_plural = _("Предложения")

    def get_show_an_active_offer(self):
        if self.validity_period < datetime.datetime.now().date():
            return self.offer


