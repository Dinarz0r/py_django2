from django.urls import path
from APIpromotions.views import PromotionListView, PromotionsDetailView

urlpatterns = [
    path('list/', PromotionListView.as_view(), name='api_promotions_list'),
    path('list/<int:pk>/', PromotionsDetailView.as_view(), name='api_promotions_detail'),

]
