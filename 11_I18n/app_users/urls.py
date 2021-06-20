from django.urls import path

from app_users.views import restore_password, login_view

urlpatterns = [
    path('restore_password/', restore_password, name='restore_password'),
    path('login_view/', login_view, name='login_view'),
]
