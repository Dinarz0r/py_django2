from _csv import reader

from django import forms
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from .forms import AddBlog, AddImageForm
from .models import ImagesModel, Blog, UserModel
from app_media.forms import UploadFileForm


def add_new_blog_view(request):
    """
    Вьюха добавления блога!
    С полем добавления множества изображений.
    """
    if request.method == "POST" and request.user.is_authenticated:
        form_blog = AddBlog(request.POST)
        form_image = AddImageForm(request.POST, request.FILES)
        if form_blog.errors or form_image.errors:
            return render(request, 'blog/new_blog.html',
                          {'blog_form': form_blog, 'add_image_form': form_image})
        elif form_blog.is_valid():
            form_blog = form_blog.save(commit=False)
            form_blog.user_id = request.user.id
            form_blog.save()
            if form_image.is_valid():
                files = request.FILES.getlist('image')
                for img in files:
                    instance = ImagesModel(image=img, blog=form_blog)
                    instance.save()
            return redirect('main_page')
    else:
        if request.user.is_authenticated:
            blog_form = AddBlog()
            add_image_form = AddImageForm()
            return render(request, 'blog/new_blog.html', {'blog_form': blog_form, 'add_image_form': add_image_form})
        else:
            return HttpResponse('У Вас не достаточно прав для добавления нового блога')


class MainViewList(ListView):
    template_name = 'blog/main_list.html'
    model = Blog
    context_object_name = 'form'
    queryset = Blog.objects.all()[:20]


def blog_detail(request, pk):
    """
    Выводим детальную страницу блога
    """
    blog = get_object_or_404(Blog, id=pk)
    image = ImagesModel.objects.filter(blog_id=pk)
    ava = 'anonymous'
    if blog.user:
        ava = UserModel.objects.filter(user_id__exact=blog.user.id)
        if ava:
            ava = ava[0]
    return render(request, 'blog/detail_blog.html', {'blog': blog,
                                                     'image': image,
                                                     'ava': ava})


def add_mass_blog_using_csv(request):
    """
     вьюха для загрузки новостей через csv.
     (реализуйте возможность загрузить несколько записей блога одним файлом csv.
     В нем должно быть две колонки: текст и дата публикации
     для добавления нужно составить таблицу строка формата 'Блог который мы заслужили 3:2021-06-01'
    """

    if request.method == "POST" and request.user.is_authenticated:
        upload_form_blog = UploadFileForm(request.POST, request.FILES)

        if upload_form_blog.is_valid():
            file_str = upload_form_blog.cleaned_data['file'].read()
            blog_str_title_and_date_publications = file_str.decode('utf-8').split('\n')
            csv_reader_blog = reader(blog_str_title_and_date_publications, delimiter=":", quotechar='"')
            for blog in csv_reader_blog:
                title, date = blog[0], blog[1]
                instance = Blog.objects.create(title=title[:100], text=title[:3000], publication_date=date,
                                               user_id=request.user.id)
                instance.save()
            return redirect('main_page')

        else:
            return render(request, 'blog/new_blog.html', {'form': upload_form_blog})
    else:
        if request.user.is_authenticated:
            csv_blog_form = UploadFileForm()
            csv_blog_form.fields['title'].widget = forms.HiddenInput()
            return render(request, 'blog/add_csv_blog.html', {'form': csv_blog_form})
        else:
            return HttpResponse('У Вас не достаточно прав для добавления нового блога')
