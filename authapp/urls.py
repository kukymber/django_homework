from django.urls import path

from authapp.views import login, logout, register
from mainapp.views import products


app_name = 'authapp'
urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    # path('detail/', products, name='detail'),
]
