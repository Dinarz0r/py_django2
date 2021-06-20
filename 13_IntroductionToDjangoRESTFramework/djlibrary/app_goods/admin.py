from django.contrib import admin
from app_goods.models import Item, ItemGroupModel


class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class ItemGroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'group_name']


admin.site.register(Item, ItemAdmin)
admin.site.register(ItemGroupModel, ItemGroupAdmin)
