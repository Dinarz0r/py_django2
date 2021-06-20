from django.urls import path
from app_goods.views import ItemList, ItemGroupList, ItemDetail
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('items/', ItemList.as_view(), name='items_list'),
    path('group_items/', ItemGroupList.as_view(), name='group_list'),
    path('items/<int:pk>/', ItemDetail.as_view(), name='detail_list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
