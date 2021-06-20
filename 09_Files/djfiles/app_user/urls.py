from django.urls import path
from .views import LoginModel, register_view, EditAccountInfo, LogoutModel

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', LoginModel.as_view(), name='login'),
    path('logout/', LogoutModel.as_view(), name='logout'),
    path('edit/', EditAccountInfo.as_view(), name='edit_account')
]
