from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import AddNewsForm, CommentFormAuth, CommentFormNonAuth
from .models import News, Comments


class NewsListView(ListView):
    """
    Выводим на странице news_list.html последние 10 объявлений.
    """
    model = News
    template_name = 'news/news_list.html'
    context_object_name = 'news_list'
    queryset = News.objects.all()[:10]


class NewsFormView(View):
    """
    Представление страницы добавление новости
    """
    model = News

    def get(self, request):
        """
        отобразим форму добавления новости
        """
        news_form = AddNewsForm()

        return render(request, 'news/add_news.html', context={'news_form': news_form})

    def post(self, request):
        """
        при методе post и верно заполненной формы добавим новость в модель NewsModel
        """
        news_form = AddNewsForm(request.POST)

        if news_form.is_valid():
            # Совершаем какую либо бизнес логику
            # например сохранение в бд
            print('ВАЛИДНО')
            news_form = news_form.save(commit=False)
            if request.user.is_authenticated:
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
        if request.user.is_authenticated:
            form = CommentFormAuth()
        else:
            form = CommentFormNonAuth()
    return render(request, 'news/new_single.html', {'new': new, "comments": comment, 'form': form})


class EditNewsForm(View):
    """
    Представление редактирования новости.
    """

    def get(self, request, news_id):
        news = News.objects.get(id=news_id)
        news_form = AddNewsForm(instance=news)
        return render(request, 'news/edit_news.html', context={'news_form': news_form, 'news_id': news_id})

    def post(self, request, news_id):
        news = News.objects.get(id=news_id)
        news_form = AddNewsForm(request.POST, instance=news)
        if news_form.is_valid():
            news_form.save()
            return redirect(f'/news/{news_id}')
        return render(request, 'news/edit_news.html', context={'news_form': news_form, 'news_id': news_id})


class LoginViewForm(LoginView):
    pass


class LogoutSessionView(LogoutView):
    next_page = '/'
