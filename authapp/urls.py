from django.urls import path

from authapp.views import Logout, ProfileFormView, LoginGBView, RegisterView
from mainapp.views import index

app_name = "authapp"

urlpatterns = [
     path('login/', LoginGBView.as_view(), name='login'),
     path('register/', RegisterView.as_view(), name='register'),
     path('profile/', ProfileFormView.as_view(), name='profile'),
     path('logout/', Logout.as_view(), name='logout'),
     path('index/', index, name='index'),
     path('verify/<str:email>/<str:activate_key>/', RegisterView.verify, name='verify'),

]
