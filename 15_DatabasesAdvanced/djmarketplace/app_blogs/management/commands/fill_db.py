from itertools import count
import time
from app_blogs.models import Blog
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        start = time.time()
        add_blog = []
        for i in count(1):
            if i > 10000:
                break
            add_blog.append(Blog(name=f'Блог новоый {i}'))
            print(i)

        Blog.objects.bulk_create(add_blog)
        print('hello')
        print(time.time() - start)
