from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Advertisement


class AdvertisementIndex(TemplateView):
    """
    Выводим стартовую страницу
    """
    template_name = 'advertisements/index.html'


class AdvertisementListView(ListView):
    """
    Выводим на странице advertisements_list.html первые 5 объявлений.
    """
    model = Advertisement
    template_name = 'advertisements/advertisements_list.html'
    context_object_name = 'advertisement_list'
    queryset = Advertisement.objects.all()[:5]


class AdvertisementDetailView(DetailView):
    model = Advertisement
    template_name = 'advertisements/advertisements_detail.html'
    context_object_name = 'adv_obj'

    def get_object(self, queryset=None):
        """
        При просмотре объявления добавляем к счетчику просмотра +1 в БД sqlite
        """
        obj = super().get_object(queryset)
        obj.view_count += 1
        obj.save()
        return obj
