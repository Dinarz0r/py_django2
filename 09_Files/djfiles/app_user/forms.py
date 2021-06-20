from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class RegForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Имя')
    last_name = forms.CharField(max_length=30, required=True, help_text='Фамилия')
    city = forms.CharField(max_length=30, required=False, help_text="Город")
    telephone = forms.CharField(max_length=30, required=True, help_text='Телефон')
    username = forms.CharField(max_length=20, help_text='Аккаунт')
    email = forms.EmailField(help_text='Эл. почта')
    avatar = forms.ImageField(help_text='Аватар', required=False)

    class Meta:
        model = User
        fields = (
        'username', 'first_name', 'last_name', 'avatar', 'email', 'city', 'telephone', 'password1', 'password2')


class EditAccountForm(forms.ModelForm):
    """
    Форма для редактирования Имени и фамилии

    """

    class Meta:
        model = User
        fields = ('first_name', 'last_name',)
