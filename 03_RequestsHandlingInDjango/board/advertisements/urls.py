from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainIndex.as_view()),
    path('advertisements/', views.Advertisements.as_view()),
    path('сontacts/', views.Contacts.as_view()),
    path('about/', views.About.as_view()),
    path('categories', views.Categories.as_view()),
    path('regions/', views.Regions.as_view())
]
