from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
import datetime

from django.views.generic import DetailView, ListView

from adminapp.mixin import BaseClassContextMixin, CustomDispatchMixin
from mainapp.models import Product, ProductCategory


# class Index(ListView, BaseClassContextMixin, CustomDispatchMixin):
#     template_name = "mainapp/index.html"
#     title = 'GeekShop Store'
#     data_time = {'data_time_now': datetime.datetime.now().strftime("%d-%m-%Y %H:%M")}
#     text = 'Новые образы и лучшие бренды на GeekShop Store. ' \
#            'Бесплатная доставка по всему миру! Аутлет: до -70% Собственный бренд. -20% новым покупателям.'
#     button_name = 'Начать покупки'


def index(request):
    data_time = {'data_time_now': datetime.datetime.now().strftime("%d-%m-%Y %H:%M")}
    content = {
        'title': 'GeekShop',
        'data_time': data_time

    }
    return render(request, "mainapp/index.html", content)


def products(request, id_category=None, page=1):
    if id_category:
        products = Product.objects.filter(category_id=id_category)
    else:
        products = Product.objects.all()

    pagination = Paginator(products, per_page=2)

    try:
        product_pagination = pagination.page(page)
    except PageNotAnInteger:
        product_pagination = pagination.page(1)
    except EmptyPage:
        product_pagination = pagination.page(pagination.num_pages)
    data_time = {'data_time_now': datetime.datetime.now().strftime("%d-%m-%Y %H:%M")}

    content = {
        'title': 'Geekshop - Каталог',
        'categories': ProductCategory.objects.all(),
        'products': product_pagination,
        'data_time': data_time
    }

    return render(request, "mainapp/products.html", content)


class ProductDetail(DetailView):
    model = Product
    template_name = 'mainapp/detail.html'
