from django.urls import path
from .views import NewsFormView, NewsListView, new_single, EditNewsForm, LoginViewForm, LogoutSessionView

urlpatterns = [
    path('', NewsListView.as_view(), name='index'),
    path('news/add_news', NewsFormView.as_view(), name='add_news'),
    path("news/<int:pk>", new_single, name='news-detail'),
    path('news/<int:news_id>/edit', EditNewsForm.as_view(), name='edit-news'),
    path('profile/login', LoginViewForm.as_view(), name='login'),
    path('profile/logout', LogoutSessionView.as_view(), name='logout'),
]