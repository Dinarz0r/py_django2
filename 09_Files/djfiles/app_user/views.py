from django.contrib.auth import login, authenticate
from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.views import LogoutView, LoginView
from django.views.generic import TemplateView
from .models import UserModel

from .forms import RegForm, EditAccountForm


class LoginModel(LoginView):
    template_name = 'profile/login.html'


class LogoutModel(LogoutView):
    next_page = '/'


def register_view(request):
    if request.method == 'POST':
        form = RegForm(request.POST, request.FILES)
        if form.is_valid():
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
            return HttpResponse('Прежде чем что то менять, аутентифицируйся ')

    def post(self, request, *args, **kwargs):
        user = request.user
        acc_form = EditAccountForm(request.POST)
        if acc_form.is_valid():
            user.last_name = acc_form.cleaned_data['last_name']
            user.first_name = acc_form.cleaned_data['first_name']
            user.save()
        return render(request, 'profile/edit_account.html', context={'form': acc_form})
