from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def products(request):
    return render(request, "products.html")


def state_words(request):
    context = {
        'name_of_link': 'Geekshop',
        'catalog': 'Каталог',
        'log_in': 'Войти'
    }
