# Generated by Django 3.2.4 on 2021-06-12 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemGroupModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=70, verbose_name='Группа товаров')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('weight', models.FloatField(verbose_name='Вес')),
                ('group_name', models.ManyToManyField(blank=True, null=True, related_name='test', related_query_name='name1', to='app_goods.ItemGroupModel', verbose_name='Группа товара')),
            ],
        ),
    ]
