import django_filters
from app_library.models import BookModel


class BookFilter(django_filters.FilterSet, django_filters.CharFilter):
    """
    Класс фильтрации поиска в DRF по полям в модели BookModel:
    title - по названию книги
    author__surname - по фамилии автора
    count_pages__gt - по кол-ву листов в книге больше чем ..
    count_pages__lt - по кол-ву листов в книге меньше чем ..
    count_pages - поиск по кол-ву листов в книге
    """
    title = django_filters.CharFilter(lookup_expr='icontains', label='Название книги:')
    count_pages__gt = django_filters.NumberFilter(field_name='count_pages', lookup_expr='gt',
                                                  label='Количество листов больше:')
    count_pages__lt = django_filters.NumberFilter(field_name='count_pages', lookup_expr='lt',
                                                  label='Количество листов меньше:')
    count_pages = django_filters.NumberFilter(field_name='count_pages', label='Количество листов:')
    author = django_filters.CharFilter(field_name='author__surname', lookup_expr='icontains', label='Фамилия автора:')

    class Meta:
        model = BookModel
        fields = ['title', 'author', 'count_pages', 'count_pages__gt', 'count_pages__lt']
