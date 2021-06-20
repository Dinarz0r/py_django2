from django.contrib.auth import login, authenticate
from django import forms
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.views import LogoutView, LoginView
from django.views.generic import TemplateView
from django.utils.translation import gettext_lazy as _
from .models import UserModel
from .forms import RegForm, EditAccountForm, RestorePasswordForm


class LoginModel(LoginView):
    template_name = 'profile/login.html'


class LogoutModel(LogoutView):
    next_page = '/'


def register_view(request):
    if request.method == 'POST':
        form = RegForm(request.POST, request.FILES)
        print(form.errors)
        if form.errors:
            return render(request, 'profile/reg_page.html',
                          {'form': form})
        elif form.is_valid():
            user = form.save()
            city = form.cleaned_data.get('city')
            telephone = form.cleaned_data.get('telephone')
            ava = form.cleaned_data.get('avatar')
            print(ava)
            UserModel.objects.create(
                user=user,
                city=city,
                telephone=telephone,
                avatar=ava,
            )
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    else:
        form = RegForm()
        context = {'form': form}
        return render(request, 'profile/reg_page.html', context=context)


class EditAccountInfo(TemplateView):
    model = RegForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user = request.user
            acc_form = EditAccountForm(instance=user)
            return render(request, 'profile/edit_account.html', context={'form': acc_form})
        else:
            return HttpResponse(_('Прежде чем что то менять, аутентифицируйся '))

    def post(self, request, *args, **kwargs):
        user = request.user
        acc_form = EditAccountForm(request.POST)
        if acc_form.is_valid():
            user.last_name = acc_form.cleaned_data['last_name']
            user.first_name = acc_form.cleaned_data['first_name']
            user.save()
        return render(request, 'profile/edit_account.html', context={'form': acc_form})


def restore_password(request):
    if request.method == 'POST':
        form = RestorePasswordForm(request.POST)
        if form.is_valid():
            # сгенерируем новый пароль с помощью метода makerandom_password в менеджере модели юзер
            new_password = User.objects.make_random_password()
            user_email = form.cleaned_data['email']
            current_user = User.objects.filter(email=user_email).first()
            if current_user:
                current_user.set_password(new_password)
                current_user.save()
            send_mail(
                subject=_('Восстановление пароля'),  # Тема
                message='Test',  # Тело письма
                from_email='admin@company.ru',  # От кого отправлено письмо
                recipient_list=[form.cleaned_data['email']],  # Список получателей
            )
            return HttpResponse(_('Письмо с восстановлением пароля успешно отправлено'))
    restore_password_form = RestorePasswordForm()
    context = {
        'form': restore_password_form
    }
    return render(request, 'profile/restore_password.html', context=context)
