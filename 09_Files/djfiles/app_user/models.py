from django.contrib.auth.models import User
from django.db import models


class UserModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField('Город', max_length=20, blank=True)
    telephone = models.CharField('Телефон', max_length=20, blank=False)
    avatar = models.ImageField('Аватарка', upload_to='avatars/', blank=True, null=True)

