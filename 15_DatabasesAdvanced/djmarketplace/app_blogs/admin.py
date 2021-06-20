from django.contrib import admin
from app_blogs.models import Post, Blog, Author, Moderator, Profile


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', ]


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class ModeratorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'verification', 'points_status']


admin.site.register(Post, PostAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Moderator, ModeratorAdmin)
admin.site.register(Profile, ProfileAdmin)
