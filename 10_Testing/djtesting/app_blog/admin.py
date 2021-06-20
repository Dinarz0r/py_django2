from django.contrib import admin
from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'create_at', 'publication_date', 'publish_flag',)


admin.site.register(Blog, BlogAdmin)
