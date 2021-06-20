from rest_framework import serializers
from app_library.models import AuthorModel, BookModel


class AuthorSerializer(serializers.ModelSerializer):
    """
    Класс сериализатора Автора
    """

    class Meta:
        model = AuthorModel
        fields = ('id', 'name', 'surname', 'date_bd',)


class BookSerializer(serializers.ModelSerializer):
    """
    Класс сериализатора Книги
    """
    author_surname = serializers.CharField(source='author.surname')
    author_name = serializers.CharField(source='author.name')

    class Meta:
        model = BookModel
        fields = ('id', 'title', 'date_release', 'count_pages', 'isbn', 'author_surname', 'author_name', 'author')
        # depth = 1
