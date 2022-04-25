from django.urls import path

from adminapp.views import admin_users, admin_users_create, admin_users_update, admin_users_delete, index, \
    admin_product_category, admin_products

app_name = 'adminapp'
urlpatterns = [
    path('', index, name='index'),
    path('users/', admin_users, name='admin_users'),
    path('users-create/', admin_users_create, name='admin_users_create'),
    path('users-update/<int:id>/', admin_users_update, name='admin_users_update'),
    path('users-delete/<int:id>/', admin_users_delete, name='admin_users_delete'),
    path('product_category/', admin_product_category, name='admin_product_category'),
    path('products/', admin_products, name='admin_products'),
]
