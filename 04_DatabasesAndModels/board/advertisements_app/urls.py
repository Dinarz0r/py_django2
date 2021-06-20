from django.urls import path
from .views import AdvertisementListView, AdvertisementDetailView, AdvertisementIndex

urlpatterns = [
    path('', AdvertisementIndex.as_view()),
    path("advertisements/", AdvertisementListView.as_view(), name='advertisement'),
    path("advertisements/<int:pk>", AdvertisementDetailView.as_view(), name='advertisement-detail'),

]
