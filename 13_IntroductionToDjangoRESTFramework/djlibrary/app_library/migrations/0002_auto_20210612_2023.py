# Generated by Django 3.2.4 on 2021-06-12 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmodel',
            name='date_release',
            field=models.IntegerField(verbose_name='Год выпуска'),
        ),
        migrations.AlterField(
            model_name='bookmodel',
            name='isbn',
            field=models.IntegerField(default=792302177),
        ),
    ]