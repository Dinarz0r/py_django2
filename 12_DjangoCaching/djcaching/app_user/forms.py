from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _


class RegForm(UserCreationForm):
    first_name = forms.CharField(label=_('Имя'), max_length=30, required=True)
    last_name = forms.CharField(label=_('Фамилия'), max_length=30, required=True)
    city = forms.CharField(label=_("Город"), max_length=30, required=False)
    telephone = forms.CharField(label=_('Телефон'), max_length=30, required=True)
    username = forms.CharField(label=_('Аккаунт'), max_length=20)
    email = forms.EmailField(label=_('Эл. почта'))
    balance = forms.DecimalField(label=_('Внести баланс'), max_digits=10, decimal_places=2)

    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'balance', 'email', 'city', 'telephone', 'password1', 'password2'
        )


class EditAccountForm(forms.ModelForm):
    """
    Форма для редактирования Имени и фамилии

    """

    class Meta:
        model = User
        fields = ('first_name', 'last_name',)


class RestorePasswordForm(forms.Form):
    email = forms.EmailField(label=_('Эл. Почта'))
