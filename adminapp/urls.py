from django.urls import path

from adminapp.views import UserListView, UserCreateView, UserUpdateView, UserDeleteView, \
    admin_product_category, admin_products, IndexTemplateView

app_name = 'adminapp'
urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('users-create/', UserCreateView.as_view(), name='admin_users_create'),
    path('users-update/<int:pk>/', UserUpdateView.as_view(), name='admin_users_update'),
    path('users-delete/<int:pk>/', UserDeleteView.as_view(), name='admin_users_delete'),
    path('product_category/', admin_product_category, name='admin_product_category'),
    path('products/', admin_products, name='admin_products'),
]
