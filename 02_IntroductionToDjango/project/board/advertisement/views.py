from django.shortcuts import render
from django.http import HttpResponse


def main(request, *args, **kwargs):
    return render(request, 'advertisement/index.html', {})


def advertisement_list(request, *args, **kwargs):
    return render(request, 'advertisement/...advertisements_list.html', {})


def profession_python(request, *args, **kwargs):
    return render(request, 'advertisement/profession_python.html', {})


def sql(request, *args, **kwargs):
    return render(request, 'advertisement/sql.html', {})


def java(request, *args, **kwargs):
    return render(request, 'advertisement/java.html', {})


def bd(request, *args, **kwargs):
    return render(request, 'advertisement/bd.html', {})


def frontend(request, *args, **kwargs):
    return render(request, 'advertisement/frontend.html', {})
