from django.urls import path
from app_library.views import AuthorList, BookList
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('authors/', AuthorList.as_view(), name='author_list'),
    path('book/', BookList.as_view(), name='book_list'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
