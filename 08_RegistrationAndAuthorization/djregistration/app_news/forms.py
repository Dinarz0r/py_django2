from django import forms
from .models import Comments, News


class AddNewsForm(forms.ModelForm):
    """
    Форма для добавления новости на основе модели NewsModel

    """

    class Meta:
        model = News
        fields = ('title', 'text', 'tags', 'activity_flag')


class CommentFormAuth(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('text',)


class CommentFormNonAuth(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('username', 'text',)
