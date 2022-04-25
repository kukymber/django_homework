from django.urls import reverse

from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render
# Create your views here.

from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm
from authapp.models import User
from mainapp.models import Product, ProductCategory


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'adminapp/admin.html')


@user_passes_test(lambda u: u.is_superuser)
def admin_users(request):
    content = {
        'title': 'Админка | Пользователи',
        'users': User.objects.all()
    }
    return render(request, 'adminapp/admin-users-read.html', context=content)


@user_passes_test(lambda u: u.is_superuser)
def admin_users_create(request):
    if request == 'POST':
        form = UserAdminRegisterForm(data=request.POST, files=request.FIELS)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_users'))
    else:
        form = UserAdminRegisterForm()
    content = {
        'title': 'Админка | Регистрация ',
        'form': form
    }

    return render(request, 'adminapp/admin-users-create.html', context=content)


@user_passes_test(lambda u: u.is_superuser)
def admin_users_update(request, id):
    user_select = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserAdminProfileForm(date=request.POST, instance=user_select, files=request.FIELS)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_users'))
    else:
        form = UserAdminProfileForm(instance=user_select)

    content = {
        'title': 'Админка | Обновление пользователя',
        'form': form
    }
    return render(request, 'adminapp/admin-users-update-delete.html', context=content)


@user_passes_test(lambda u: u.is_superuser)
def admin_users_delete(request, id):
    user = User.objects.get(id=id)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('adminapp:admin_users'))


def admin_product_category(request):
    context = {
        'title': 'Админка | Категории',
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'adminapp/product_category.html', context)


def admin_products(request):
    context = {
        'title': 'Админка | Продукты',
        'products': Product.objects.all(),
    }
    return render(request, 'adminapp/products.html', context)
