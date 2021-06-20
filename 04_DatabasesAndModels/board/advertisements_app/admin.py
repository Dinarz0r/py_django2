from django.contrib import admin
from .models import Advertisement, AdvertisementStatus, AdvertisementUser, AdvertisementCategories


# Register your models here.
# @admin.register(Advertisement)
# class AdvertisementAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(AdvertisementStatus)
# class AdvertisementStatusAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(AdvertisementUser)
# class AdvertisementStatusAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(AdvertisementCategories)
# class AdvertisementStatusAdmin(admin.ModelAdmin):
#     pass

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'user']


admin.site.register(Advertisement, AdvertisementAdmin)
