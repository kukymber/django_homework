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
    # products = [
    #     {'name': 'Худи черного цвета с монограммами adidas Originals.',
    #      'text': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
    #      'price': '6 090,00 руб.',
    #      'link': 'vendor/img/products/Adidas-hoodie.png'
    #      },
    #     {'name': 'Синяя куртка The North Face',
    #      'text': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
    #      'price': '23 725,00 руб.',
    #      'link': 'vendor/img/products/Blue-jacket-The-North-Face.png'
    #      },
    #     {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
    #      'text': 'Материал с плюшевой текстурой. Удобный и мягкий.',
    #      'price': '3 390,00 руб.',
    #      'link': 'vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png'
    #      },
    #     {'name': 'Черный рюкзак Nike Heritage',
    #      'text': 'Плотная ткань. Легкий материал.',
    #      'price': '6 090,00 руб.',
    #      'link': 'vendor/img/products/Black-Nike-Heritage-backpack.png'
    #      },
    #     {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
    #      'text': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
    #      'price': '13 590,00 руб.',
    #      'link': 'vendor/img/products/Black-Dr-Martens-shoes.png'
    #      },
    #     {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
    #      'text': 'Легкая эластичная ткань сирсакер Фактурная ткань.',
    #      'price': '2 890,00 руб.',
    #      'link': 'vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png'
    #      }
    #
    #
    # ]
    data_time = {'data_time_now': datetime.datetime.now().strftime("%d-%m-%Y %H:%M")}
    content = {
        'title': 'Geekshop - Каталог',
        'categories': categories,
        'products': products,
        'data_time': data_time
     }

    return render(request, "products.html", context=content)


