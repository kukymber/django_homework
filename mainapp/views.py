from django.shortcuts import render
import datetime

from mainapp.models import Product, ProductCategory


def index(request):
    data_time = {'data_time_now': datetime.datetime.now().strftime("%d-%m-%Y %H:%M")}
    content = {

        'name_of_shop': 'GeekShop Store',
        'text': 'Новые образы и лучшие бренды на GeekShop Store.'
                'Бесплатная доставка по всему миру! Аутлет: до -70% Собственный бренд. -20% новым покупателям.',
        'button_name': 'Начать покупки',
        'data_time': data_time

    }
    return render(request, "index.html", context=content)


def products(request):
    categories = ProductCategory.objects.all()
    products = Product.objects.all()

    data_time = {'data_time_now': datetime.datetime.now().strftime("%d-%m-%Y %H:%M")}

    content = {
        'title': 'Geekshop - Каталог',
        'categories': categories,
        'products': products,
        'data_time': data_time
     }

    return render(request, "products.html", context=content)


