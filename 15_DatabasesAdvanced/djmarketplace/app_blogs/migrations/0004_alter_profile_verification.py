# Generated by Django 3.2.4 on 2021-06-17 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blogs', '0003_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='verification',
            field=models.CharField(choices=[('newbie', 'Новичок'), ('Advanced', 'Продвинутый'), ('Expert', 'Эксперт')], default='newbie', max_length=10, verbose_name='Флаг верификации'),
        ),
    ]
