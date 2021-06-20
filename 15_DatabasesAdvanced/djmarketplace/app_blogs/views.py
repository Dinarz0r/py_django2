from django.db import transaction
from django.shortcuts import render
from django.views.generic import ListView
from app_blogs.models import Post, Profile, Blog
from app_blogs.utils import up_points, down_points, assign_a_status
from django.db.models import Avg, Count



class BlogInfoListView(ListView):
    model = Blog
    queryset = Blog.objects.annotate(count_posts=Count('posts'))
    context_object_name = 'blogs'
    template_name = 'app_blog/blog_count.html'

class MainListView(ListView):
    model = Post

    # queryset = Post.objects.select_related('blog').prefetch_related('author').select_related('moderator').all()
    # context_object_name = 'form'
    # template_name = 'app_blog/blog.html'

    # def get_queryset(self):
    #     assigning_a_status(user_id=2)
    #     return self
    def get(self, request, *args, **kwargs):
        queryset = Post.objects.select_related('blog').prefetch_related('author').select_related('moderator').all()
        context = {'form': queryset}
        # транзакции
        # with transaction.atomic():
        #     up_points(request.user.id, 3000)
        #     assign_a_status(request.user.id)
        # post = Post.objects.only('author').all()
        # for p in post:
        #     print(p.author.all())

        # тут мы считаем среднее кол-во лайков из всех постов
        # likes = Post.objects.aggregate(avg_likes=Avg('likes_count'))



        return render(request, 'app_blog/blog.html', context=context)
