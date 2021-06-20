# Generated by Django 2.2 on 2021-05-30 21:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, max_length=20, verbose_name='Город')),
                ('telephone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Баланс')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Модель пользователя',
                'verbose_name_plural': 'Модель пользователей',
            },
        ),
    ]
