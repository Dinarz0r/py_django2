# Generated by Django 2.2 on 2021-05-04 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements_app', '0003_advertisement_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisementuser',
            name='advertisement',
        ),
    ]
