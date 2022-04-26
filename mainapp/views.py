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
    return render(request, "mainapp/index.html", context=content)


def products(request, id_category=None):
    if id_category:
        products_ = Product.objects.filter(category_id=id_category)
    else:
        products_= Product.objects.all()

    categories = ProductCategory.objects.all()
    # products = Product.objects.all()

    data_time = {'data_time_now': datetime.datetime.now().strftime("%d-%m-%Y %H:%M")}

    content = {
        'title': 'Geekshop - Каталог',
        'categories': categories,
        'products': products_,
        'data_time': data_time,
     }

    return render(request, "mainapp/products.html", context=content)


