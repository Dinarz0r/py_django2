import requests
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.views import View
from django.views.generic import ListView, FormView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import AddNewsForm, CommentFormAuth, CommentFormNonAuth
from .models import News, Comments, Tag
from django import forms


class NewsListView(ListView):
    """
    Выводим на странице news_list.html новости
    """
    model = News

    def get(self, request, *args, **kwargs):
        news_form = None
        flag_auth = False
        tag = Tag.objects.all()
        if request.user.is_authenticated:
            news_form = News.objects.filter(activity_flag__icontains=1)
            flag_auth = True
            if not request.user.has_perm('app_news.can_publish'):
                pass
            else:
                news_form = News.objects.all()

        return render(request, 'news/news_list.html',
                      context={'news_list': news_form, 'tags': tag, 'flag_auth': flag_auth})

    def post(self, request, *args, **kwargs):
        news_form = None
        flag_auth = True
        filter_req_tag = request.POST['filter']
        # выводим список отфильтрованного контента
        form_for_tag = News.objects.filter(tags__id__iexact=filter_req_tag)
        if form_for_tag:
            news_form = form_for_tag
        elif request.POST['filter'] == 'date':
            news_form = News.objects.filter(activity_flag__icontains=1)
            if not request.user.has_perm('app_news.can_publish'):
                pass
            else:
                news_form = News.objects.all()
        elif request.POST['filter'] == 'all-news':
            news_form = News.objects.all()
        form_search_tags = Tag.objects.all()
        return render(request, 'news/news_list.html',
                      context={'news_list': news_form, 'tags': form_search_tags, 'flag_auth': flag_auth})


class NewsFormView(FormView):
    """
    Представление страницы добавление новости
    """
    model = News

    def get(self, request, *args, **kwargs):
        """
        отобразим форму добавления новости
        """

        if not request.user.has_perm('app_news.add_news'):
            return HttpResponse('У вас недостаточно прав для создания новости обратитесь к администратору сайта')
        else:
            news_form = AddNewsForm()
        if not request.user.has_perm('app_news.can_publish'):
            news_form.fields['activity_flag'].widget = forms.HiddenInput()


        return render(request, 'news/add_news.html', context={'news_form': news_form})


    def post(self, request, *args, **kwargs):
        """
        при методе post и верно заполненной формы добавим новость в модель NewsModel
        """
        news_form = AddNewsForm(request.POST)

        if news_form.is_valid():
            # Совершаем какую либо бизнес логику
            # например сохранение в бд
            # profile при добавлении новости прибавляем счетчик кол-ва добавленных новостей
            profile = request.user.profile
            profile.count_published_news += 1
            profile.save()
            # news_form тут сохраняем новость в бд и присваиваем новости user_id
            news_form = news_form.save(commit=False)
            news_form.user_id = request.user.id
            news_form.save()
            return redirect('index')
        return render(request, 'news/add_news.html', context={'news_form': news_form})


def new_single(request, pk):
    """
    Выводим детальную страницу новости+комментарии к ней
    (с возможностью добавить новый комментарий).
    """
    new = get_object_or_404(News, id=pk)
    comment = Comments.objects.filter(new=pk)
    flag_moder = False
    if request.method == "POST":
        if request.user.is_authenticated:
            form = CommentFormAuth(request.POST)  # тут принимаем заполненную форму коммента
        else:
            form = CommentFormNonAuth(request.POST)
        if form.is_valid():
            form = form.save(commit=False)  # commit=False приостановить сохранение формы
            if request.user.is_authenticated:
                form.username = request.user  # присваиваем имя пользователя который сейчас на сайте
                form.user_id = request.user.id  # присваиваем id залогиненного пользователя
            form.new = new  # к какой статье присваиваем наш комментарий
            form.save()
            return redirect(new_single, pk)
    else:
        form = CommentFormAuth()
        if request.user.is_authenticated:
            if not request.user.has_perm('app_news.can_publish'):
                pass
            else:
                flag_moder = True

            return render(request, 'news/new_single.html', {'new': new,
                                                            "comments": comment,
                                                            'form': form,
                                                            'flag': flag_moder})
        else:
            return HttpResponse('Для просмотра контента необходимо аутентифицироваться')


class EditNewsForm(View):
    """
    Представление редактирования новости.
    необходимы права has_perm('app_news.can_publish') т.е. (Для модераторов)
    """

    def get(self, request, news_id):
        if not request.user.has_perm('app_news.can_publish'):
            return HttpResponse("Для редактирования новости у вас не достаточно прав!")
        news = News.objects.get(id=news_id)
        news_form = AddNewsForm(instance=news)
        return render(request, 'news/edit_news.html', context={'news_form': news_form, 'news_id': news_id})

    def post(self, request, news_id):
        if not request.user.has_perm('app_news.can_publish'):
            return HttpResponse("Для редактирования новости у вас не достаточно прав!")
        news = News.objects.get(id=news_id)
        news_form = AddNewsForm(request.POST, instance=news)
        if news_form.is_valid():
            news_form.save()
            return redirect(f'/news/{news_id}')
        return render(request, 'news/edit_news.html', context={'news_form': news_form, 'news_id': news_id})


class LoginViewForm(LoginView):
    """
    Класс для логирования на сайт (аутентификация)
    """
    pass


class LogoutSessionView(LogoutView):
    """
    Класс для разлогирования (разрыв сессии)
    """
    next_page = '/'
