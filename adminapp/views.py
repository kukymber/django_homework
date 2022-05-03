from django.urls import reverse, reverse_lazy

from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.views.generic import ListView, TemplateView, CreateView, DetailView, UpdateView, DeleteView

from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm, ProductCreationForm
from authapp.models import User
from adminapp.mixin import BaseClassContextMixin, CustomDispatchMixin
from mainapp.models import Product, ProductCategory


class IndexTemplateView(TemplateView, BaseClassContextMixin, CustomDispatchMixin):
    template_name = 'adminapp/admin.html'
    title = 'Главная страница'


# @user_passes_test(lambda u: u.is_superuser)
# def index(request):
#     return render(request, 'adminapp/admin.html')
#

class UserListView(ListView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-read.html'
    title = 'Админка | Пользователи'
    context_object_name = 'users'


class UserCreateView(CreateView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-create.html'
    form_class = UserAdminRegisterForm
    title = 'Админка | Пользователи'
    success_url = reverse_lazy('adminapp:admin_users')


class UserUpdateView(UpdateView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    title = 'Админка | Обновление пользователя'
    success_url = reverse_lazy('adminapp:admin_users')


class UserDeleteView(DeleteView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    title = 'Админка | Обновление пользователя'
    success_url = reverse_lazy('adminapp:admin_users')

    def delete(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class ProductCreateFrom(CreateView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    template_name = 'adminapp/admin-product-create.html'
    form_class = ProductCreationForm
    title = 'Админка | Создание продукта'
    success_url = reverse_lazy('adminapp:admin_product')

    # def post(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     self.object.save()
    #     return HttpResponseRedirect(self.get_success_url())


class ProductListViews(ListView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    template_name = 'adminapp/test.html'
    title = 'Админка | Продукты'
    context_object_name = 'product'


class ProductUpdateView(UpdateView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'adminapp/admin-product-update-delete.html'
    form_class = UserAdminProfileForm
    title = 'Админка | Обновление пользователя'
    success_url = reverse_lazy('adminapp:admin_users')


def admin_product(request):
    context = {
        'title': 'Админка | Продукты',
        'products': Product.objects.all(),
    }
    return render(request, 'adminapp/admin-product-create.html', context)


def admin_product_update(request):
    pass
