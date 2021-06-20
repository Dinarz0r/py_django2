from django.urls import path
from .views import MainShopsListView, DetailShopView, DetailProductView

urlpatterns = [
    path('', MainShopsListView.as_view(), name='main_shops_page'),
    path('shop/<int:pk>', DetailShopView.as_view(), name='detail_shop_page'),
    path('shop/buy/<int:pk>', DetailProductView.as_view(), name='detail_product_page')
]
