# Generated by Django 2.2 on 2021-05-04 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
