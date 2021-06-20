import time

from django.shortcuts import render, HttpResponse, redirect
from .forms import UploadFileForm, DocumentForm, MultiFileForm
from .models import File


def upload_files(request):
    if request.method == 'POST':
        upload_file_form = UploadFileForm(request.POST, request.FILES)
        if upload_file_form.is_valid():
            file = request.FILES['file']
            return HttpResponse(
                content=f'Имя файла: {file.name} <br>Весит {file.size} байтов <br> {file.read().decode("utf-8")}',
                status=200)
    else:
        upload_file_form = UploadFileForm()

    context = {
        'form': upload_file_form
    }
    return render(request, 'media/upload_file.html', context=context)


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.file.name = time.strftime('%d%m%y-%H-%M-%S')
            form.save()

            return redirect('/')
    else:
        form = DocumentForm()
    return render(request, 'goods/file_form_upload.html', {'form': form})


def upload_files_view(request):
    if request.method == 'POST':
        form = MultiFileForm(request.POST, request.FILES)
        if form.is_valid():
            files = request.FILES.getlist('file_field')
            for f in files:
                instance = File(file=f)
                instance.save()
            return HttpResponse('Yes')
    else:
        upload_file_form = MultiFileForm()

        context = {
            'form': upload_file_form
        }
        return render(request, 'media/upload_file.html', context=context)
