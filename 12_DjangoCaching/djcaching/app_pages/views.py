from django.shortcuts import render


def welcome(request):
    return render(request, 'welcome.html')


def main_page(request):
    return render(request, 'main.html')