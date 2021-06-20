# Generated by Django 2.2 on 2021-05-27 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': 'good', 'verbose_name_plural': 'goods'},
        ),
        migrations.AlterField(
            model_name='item',
            name='code',
            field=models.CharField(max_length=100, verbose_name='code'),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='price'),
        ),
    ]