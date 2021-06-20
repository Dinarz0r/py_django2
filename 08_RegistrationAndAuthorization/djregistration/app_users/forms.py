from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='имя')
    last_name = forms.CharField(max_length=30, required=False, help_text='Фамилия')
    city = forms.CharField(max_length=30, required=False, help_text="Город")
    telephone = forms.CharField(max_length=30, required=True, help_text='Телефон')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'city', 'telephone', 'password1', 'password2')
