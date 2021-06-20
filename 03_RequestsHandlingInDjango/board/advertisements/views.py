from django.shortcuts import render
from django.views import View
from django import forms
from django.views.generic import TemplateView


class Advertisements(TemplateView):
    template_name = 'advertisements/...advertisements_list.html'
    count_click = 0
    context = {
        'job': [
            'Мастер на час',
            'Выведение из запоя',
            'Пайтон разработчик',
            'Услуги тестировщика'
        ],
        'count_click': count_click
    }

    def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)
        context = Advertisements.context
        context['count_click'] = Advertisements.count_click
        return context

    def post(self, request):
        new_reg = request.POST.get("new_reg")
        Advertisements.context['job'].append(new_reg)
        Advertisements.count_click += 1
        return render(request, 'advertisements/...advertisements_list.html',
                      {'new': 'запрос на создание новой записи успешно выполнен',
                       'count_click': Advertisements.count_click
                       })


class Contacts(TemplateView):
    template_name = 'advertisements/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['address'] = 'г. Москва, ул. Пушкина, д. Колотушкина'
        context['telephone'] = '8-800-708-19-45'
        context['email'] = 'sales@company.com'
        return context


class Regions(View):
    regions = ['Москва', 'Московская область', 'республика Алтай', 'Вологодская область']
    name = forms.CharField()
    post_zpros = ''

    def get(self, request):
        return render(request, 'advertisements/regions.html', {'regions': Regions.regions})

    def get_regions(self):
        return Regions.regions

    def post(self, request):
        new_reg = request.POST.get("new_reg")
        Regions.regions.append(new_reg)
        return render(request, 'advertisements/regions.html',
                      {'regions': Regions.regions, 'new': 'регион успешно создан'})


class About(TemplateView):
    template_name = 'advertisements/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Очумелые ручки'
        context['название'] = 'Бесплатные объявления'
        context['описание'] = 'Бесплатные объявления в вашем городе!'
        context['description'] = """
        Большинство людей, продающих на Авито свои вещи или услуги, подходят к вопросу составления объявления формально. 
        В итоге, если вы конечно не поставили заниженную цену, получение отклика приходится ждать довольно долго. 
        Продающее объявление на Авито, это текст, составленный по правилам современного торгового маркетинга. 
        Если при размещении своего предложения вы не учтете параметры востребованности товара или услуги, 
        то вашим товаром никто не заинтересуется.
        """
        return context


class Categories(View):
    categories = ['личные вещи', 'транспорт', 'хобби', 'отдых']

    def get(self, request):
        return render(request, 'advertisements/categories.html', {'categories': Categories.categories})

    def get_categories(self):
        return Categories.categories


class MainIndex(TemplateView):
    """
    метод get должен возвращать html форму, на которой должны быть представлены
    следующие элементы: выбора категории из списка, выбор региона из списка,
    текстовое поле для ввода названия объявления и кнопка “Найти”.
    (Значения для выбора нужно передавать из представления)
    """
    template_name = 'advertisements/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Categories()
        regions = Regions()
        context['get_cat'] = categories.get_categories()
        context['get_reg'] = regions.get_regions()
        return context

    def post(self, request):
        search = request.POST.get("search")
        return render(request, 'advertisements/regions.html',
                      {'new': 'input adv'})

