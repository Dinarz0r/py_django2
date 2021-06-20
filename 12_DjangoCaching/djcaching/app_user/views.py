from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView, LoginView
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView
from django.core.cache import cache
from .forms import RegForm, EditAccountForm, RestorePasswordForm
from .models import UserModel
from app_shops.models import PurchaseHistoryModel, PromotionsModel, OffersModel
import datetime
from django.db.models.signals import pre_save
from django.dispatch import receiver

promotions_cache_key_list = []
offers_cache_key_list = []


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
            balance = form.cleaned_data.get('balance')
            UserModel.objects.create(
                user=user,
                city=city,
                telephone=telephone,
                balance=balance
            )
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('main_shops_page')
    else:
        if not request.user.is_authenticated:
            form = RegForm()
            context = {'form': form}
            return render(request, 'profile/reg_page.html', context=context)
        else:
            return HttpResponse(_('Вы уже имеете аккаутнт'))


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


def personal_account_of_the_loyalty_program(request):
    if request.user.is_authenticated:
        user = UserModel.objects.filter(user_id=request.user.id).first()
        if request.user.username == 'admin':
            balance = 0
        else:
            balance = user.balance

        promotions_cache_key = f'promotions:{request.user.username}'
        offers_cache_key = f'offers:{request.user.username}'
        promotions_cache_key_list.append(promotions_cache_key)
        offers_cache_key_list.append(offers_cache_key)
        promotions = PromotionsModel.objects.filter(validity_period__gte=datetime.datetime.now().date())
        offers = OffersModel.objects.filter(validity_period__gte=datetime.datetime.now().date())

        cache.get_or_set(promotions_cache_key, promotions, 30 * 60)
        cache.get_or_set(offers_cache_key, offers, 30 * 60)
        payment_history = PurchaseHistoryModel.objects.filter(user_id=request.user.id)
        return render(request, 'profile/personal_account_of_the_loyalty_program.html',
                      context={
                          'user': user,
                          'balance': balance,
                          'promotions': promotions,
                          'payment_history': payment_history,
                          'offers': offers
                      })


@receiver(pre_save, sender=PromotionsModel)
def clear_promotions_cache(sender, **kwargs):
    """Чистим кэш при добавлении акции"""
    for i in promotions_cache_key_list:
        if i in cache:
            promotions_cache_key_list.remove(i)
            cache.delete(i)
            print('Удалили кэш акции')

@receiver(pre_save, sender=OffersModel)
def clear_offers_cache(sender, **kwargs):
    """Чистим кэш при добавлении предложения"""
    for i in offers_cache_key_list:
        if i in cache:
            offers_cache_key_list.remove(i)
            cache.delete(i)
        print('Удалили кэш предложения')