from django.contrib import admin
from app_library.models import AuthorModel, BookModel


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'surname', 'date_bd']


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'date_release', 'isbn']


admin.site.register(AuthorModel, AuthorAdmin)
admin.site.register(BookModel, BookAdmin)
