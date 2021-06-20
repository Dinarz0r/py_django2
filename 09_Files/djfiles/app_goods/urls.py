from django.urls import path
from .views import items_list, update_price, model_form_upload


urlpatterns = [
    path('items/', items_list, name='item_list'),
    path('update_price/', update_price, name='update_prices'),
    path('model_form_upload_file/', model_form_upload, name='model_form_upload_file')
]
