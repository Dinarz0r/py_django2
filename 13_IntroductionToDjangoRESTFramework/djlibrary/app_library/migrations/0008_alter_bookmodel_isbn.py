# Generated by Django 3.2.4 on 2021-06-15 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_library', '0007_auto_20210615_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmodel',
            name='isbn',
            field=models.IntegerField(default=128547811),
        ),
    ]
