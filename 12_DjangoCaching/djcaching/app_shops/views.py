from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import ShopsModel, ProductsModel, PurchaseHistoryModel
from app_user.models import UserModel
from django.utils.translation import gettext_lazy as _


class MainShopsListView(ListView):
    model = ShopsModel
    template_name = 'shops/main_page_list_shop.html'
    context_object_name = 'shops'
    queryset = ShopsModel.objects.all()[:10]


class DetailShopView(DetailView):
    model = ShopsModel
    template_name = 'shops/detail_shop_page.html'
    context_object_name = 'shop'

    def get_context_data(self, queryset=None, **kwargs):
        context = super().get_context_data(**kwargs)
        good = super().get_object(queryset)
        context['goods'] = ProductsModel.objects.filter(shop=good)
        return context


class DetailProductView(DetailView):
    model = ProductsModel
    template_name = 'shops/detail_product_page.html'
    context_object_name = 'shop'

    def get_context_data(self, queryset=None, **kwargs):
        context = super().get_context_data(**kwargs)
        product = super().get_object(queryset)
        context['shop'] = ProductsModel.objects.filter(product=product).first()
        return context

    def post(self, request, *args, **kwargs):
        product = super().get_object()
        if request.POST['buy'] and request.user.is_authenticated:
            user = UserModel.objects.filter(user_id=request.user.id).first()
            if user.balance >= product.price:
                user.balance -= product.price
                add_a_bag_to_a_user = PurchaseHistoryModel.objects.create(
                    user_id=request.user.id,
                    goods_id=product.article,
                    price=product.price,
                )
                add_a_bag_to_a_user.save()
                user.save()
                return redirect('main_shops_page')
            else:
                return HttpResponse(_('У вас не достаточно средств'))
        return render(request, 'shops/detail_product_page.html', {'shop': product})
