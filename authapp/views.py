from django.shortcuts import render


# Create your views here.
from authapp.forms import UserLoginForm


def login(request):
    content = {
        'title': 'Geekshop | Авторизация',
        'form': UserLoginForm()
    }
    return render(request, 'authapp/login.html', context=content)


def register(request):
    content = {
        'title': 'Geekshop | Регистрация'
    }
    return render(request, 'authapp/register.html', context=content)


def logout(request):
    pass
