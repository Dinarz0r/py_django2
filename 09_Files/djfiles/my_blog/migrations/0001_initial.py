# Generated by Django 2.2 on 2021-05-21 17:12

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
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('text', models.TextField(max_length=3000, verbose_name='Текст статьи')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания новости')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления статьи')),
                ('publish_flag', models.BooleanField(default=True, verbose_name='Опубликовать блог')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Блог',
                'verbose_name_plural': 'Блоги',
                'ordering': ['-create_at'],
                'permissions': (('can_publish', 'Может публиковать'),),
            },
        ),
        migrations.CreateModel(
            name='ImagesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/', verbose_name='Изображение')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_blog.Blog', verbose_name='Блог')),
            ],
        ),
    ]
