# Generated by Django 3.2.4 on 2021-06-12 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_library', '0005_auto_20210612_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmodel',
            name='isbn',
            field=models.IntegerField(default=243257710),
        ),
    ]