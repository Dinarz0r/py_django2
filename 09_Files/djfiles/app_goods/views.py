from _csv import reader
import time
from decimal import Decimal

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Item, File
from .forms import UploadpriceForm, DocumentForm


def items_list(request):
    items = Item.objects.all()
    return render(request, 'goods/items_list.html', {'items_list': items})


def update_price(request):
    if request.method == 'POST':
        upload_file_form = DocumentForm(request.POST, request.FILES)

        if upload_file_form.is_valid():

            price_file = upload_file_form.cleaned_data['file'].read()

            price_str = price_file.decode('utf-8').split('\n')
            upload_file_form = upload_file_form.save(commit=False)
            upload_file_form.file.name = f"{time.strftime('%d%m%y-%H-%M-%S')} {upload_file_form.file.name}"
            upload_file_form.save()
            csv_reader = reader(price_str, delimiter=":", quotechar='"')
            count_new_price = 0
            count_old_price = 0
            count_not_product = 0
            articul_is_not_bd = []
            for row in csv_reader:
                if Item.objects.filter(code=row[0]):
                    if Item.objects.filter(code=row[0]).get(code=row[0]).price != round(float(row[1]), 2):
                        Item.objects.filter(code=row[0]).update(price=Decimal(row[1]))
                        count_new_price += 1
                    else:

                        count_old_price += 1
                else:
                    articul_is_not_bd.append(row[0])
                    count_not_product += 1

            # Item.objects.filter(code=row[0]).update(price=Decimal(row[1]))
            return HttpResponse(content=f'Кол-во обновленных товаров: {count_new_price} шт.<br>'
                                        f'Кол-во не обновленных товаров: {count_old_price} шт.<br>'
                                        f'Артикулы товаров которых нет в БД: {articul_is_not_bd}', status=200)
    else:
        upload_file_form = DocumentForm()

        context = {
            'form': upload_file_form
        }
        return render(request, 'goods/upload_price_file.html', context=context)


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = DocumentForm()
    return render(request, 'goods/file_form_upload.html', {'form': form})
