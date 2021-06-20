from django.contrib import admin
from .models import File


class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'creat_at',)


admin.site.register(File, FileAdmin)
