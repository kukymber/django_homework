from django.urls import path
from mainapp.views import products

app_name = 'mainapp'
urlpatterns = [
    path('', products, name='products'),
    path('detail/', products, name='detail'),
    path('category/<int:id_category>/', products, name='category'),
]


def products(request, pk=None):
    print(pk)
