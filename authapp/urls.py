from django.urls import path

from authapp.views import logout, register, profile, index, LoginUserView

app_name = 'authapp'
urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    # path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),
    path('index/', index, name='index'),
]
