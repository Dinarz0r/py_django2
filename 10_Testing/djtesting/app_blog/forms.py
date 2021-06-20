from django import forms
from .models import Blog, ImagesModel
from django.utils.translation import gettext_lazy as _


class AddBlog(forms.ModelForm):
    """
    Форма добавления нового блога
    """

    title = forms.CharField(label=_('Заголовок'), min_length=5, max_length=100, required=True)
    text = forms.Textarea()

    class Meta:
        model = Blog
        fields = ('title', 'text', 'publication_date', 'publish_flag',)


class AddImageForm(forms.Form):
    image = forms.ImageField(label=_('Загрузить фото'), required=False,
                             widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = ImagesModel
        fields = ('image',)
