from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from basket.models import Basket
from mainapp.models import Product


def basket_add(request, id):
    user_select = request.user
    product = Product.objects.get(id=id)
    baskets = Basket.objects.get(user=user_select, product=product)

    if baskets:
        baskets.quantity += 1
        baskets.save()
    else:
        Basket.objects.create(user=user_select, product=product, quantity=1)
    return HttpResponseRedirect(request.Meta.get('HTTP_REFERER'))


def basket_remove(request, basket_id):
    pass
