from django.contrib import admin
from .models import ShopsModel, ProductsModel, PurchaseHistoryModel, OffersModel, PromotionsModel


class ShopsAdmin(admin.ModelAdmin):
    list_display = ['name_shop', 'telephone', 'id']


class ProductsAdmin(admin.ModelAdmin):
    pass


class PurchaseHistoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'goods']


class OffersAdmin(admin.ModelAdmin):
    list_display = ['offer', 'validity_period', 'id']


class PromotionsAdmin(admin.ModelAdmin):
    list_display = ['promotion', 'validity_period', 'id']


admin.site.register(OffersModel, OffersAdmin)
admin.site.register(PromotionsModel, PromotionsAdmin)
admin.site.register(ShopsModel, ShopsAdmin)
admin.site.register(ProductsModel, ProductsAdmin)
admin.site.register(PurchaseHistoryModel, PurchaseHistoryAdmin)
