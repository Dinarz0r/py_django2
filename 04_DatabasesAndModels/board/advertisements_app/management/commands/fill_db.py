from itertools import count
from random import randint

# from advertisements_app.models import Advertisement
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        for i in count(209892):
            if i > 500000:
                break
            add_new = Advertisement(title=f'Объявление {i}',
                                    description=f'Описание объявления {i}',
                                    price=randint(1000000, 5000000))
            add_new.save()
            print(i)


