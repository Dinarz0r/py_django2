from django.contrib import admin
from .models import UserModel


class UserModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'telephone',)


admin.site.register(UserModel, UserModelAdmin)
