from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LogoutView, LoginView
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Profile
from .forms import RegistrationForm


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            city = form.cleaned_data.get('city')
            telephone = form.cleaned_data.get('telephone')
            Profile.objects.create(
                user=user,
                city=city,
                telephone=telephone,

            )
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    else:
        form = RegistrationForm()
    return render(request, 'profiles/register.html', {'form': form})


class YouInfoView(TemplateView):
    template_name = 'profiles/users_info.html'


class IndexView(TemplateView):
    template_name = 'index.html'

class LoginModelView(LoginView):
    template_name = 'profiles/login.html'

class LogoutSessionView(LogoutView):
    next_page = '/'
