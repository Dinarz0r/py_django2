from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name='main'),
    path("advertisement/", views.advertisement_list, name='advertisement_list'),
    path("profession_python/", views.profession_python, name="profession_python"),
    path("bd/", views.bd, name="bd"),
    path("frontend/", views.frontend, name="frontend"),
    path("java/", views.java, name="java"),
    path("sql/", views.sql, name="sql"),
]
