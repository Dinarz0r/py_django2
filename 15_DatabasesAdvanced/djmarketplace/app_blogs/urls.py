from django.urls import path
from app_blogs.views import MainListView, BlogInfoListView

urlpatterns = [
    path('', MainListView.as_view(), name='index'),
    path('blog_info/', BlogInfoListView.as_view(), name='blog_info'),

]
