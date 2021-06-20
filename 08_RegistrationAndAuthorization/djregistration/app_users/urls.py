from django.urls import path
from .views import register_view, YouInfoView, IndexView, LoginModelView, LogoutSessionView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('account/', YouInfoView.as_view(), name='you-info'),
    path('register/', register_view, name='register'),
    path('login/', LoginModelView.as_view(), name='login'),
    path('logout/', LogoutSessionView.as_view(), name='logout')
]
