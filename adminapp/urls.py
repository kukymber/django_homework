from django.urls import path

from adminapp.views import admin_users, admin_user_create, admin_user_update, admin_user_delete
from authapp.views import login, logout, register, profile, index

app_name = 'authapp'
urlpatterns = [
    path('', index, name='index'),
    path('users/', admin_users, name='admin_users'),
    path('users-create/', admin_user_create, name='admin_user_create'),
    path('users-update/<int:id>/', admin_user_update, name='admin_user_update'),
    path('users-delete/<int:id>/', admin_user_delete, name='admin_user_delete'),
]