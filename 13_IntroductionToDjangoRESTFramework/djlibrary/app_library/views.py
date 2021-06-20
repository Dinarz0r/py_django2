from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from app_library.serializers import AuthorSerializer, BookSerializer
from app_library.models import AuthorModel, BookModel
from app_library.filtersAPI import BookFilter
from django_filters.rest_framework import DjangoFilterBackend


class AuthorList(ListModelMixin, CreateModelMixin, GenericAPIView):
    """
    Класс представления сериализатора Автора
    с фильтром поиска автора по имени
    """
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('name',)

    def get(self, request):
        return self.list(request)

    def post(self, request, format=None):
        return self.create(request)


class BookList(ListModelMixin, CreateModelMixin, GenericAPIView):
    """
    Класс представления сериализатора Автора
    с фильром поиска книг по кол-ву листов и по имени автора
    """
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = BookFilter

    def get(self, request):
        return self.list(request)

    def post(self, request, format=None):
        return self.create(request)
