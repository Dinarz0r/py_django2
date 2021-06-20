from django.urls import path
from .views import add_new_blog_view, MainViewList, blog_detail, add_mass_blog_using_csv

urlpatterns = [
    path('', MainViewList.as_view(), name='main_page'),
    path('blog/new_blog', add_new_blog_view, name='add_blog'),
    path("blog/<int:pk>", blog_detail, name='news-detail'),
    path('blog/add_csv_blog', add_mass_blog_using_csv, name='add_csv_blog'),

]
