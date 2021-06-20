from django.db import models


class PromotionsModel(models.Model):
    """
    Модель для хранения информации об акциях (Дата начала, Дата окончания, Процент скидки, Название)
    """
    title = models.CharField(verbose_name='Название акции', max_length=300)
    discount_percentage = models.IntegerField(verbose_name='Процент скидки')
    start_promotions_date = models.DateField(verbose_name='Начало акции')
    end_promotions_date = models.DateField(verbose_name='Конец акции')

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = "Акции"
        ordering = ['-start_promotions_date']
        permissions = (
            ('can_publish', "Может публиковать"),
        )
