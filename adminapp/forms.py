from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from authapp.models import User


class UserAdminRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'last_name', 'first_name', 'email', 'image', 'age')

    def __init__(self, *args, **kwargs):
        super(UserAdminRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = "Введите имя пользователя"
        self.fields['password1'].widget.attrs['placeholder'] = "Введите пароль"
        self.fields['password2'].widget.attrs['placeholder'] = "Повторите пароль"
        self.fields['last_name'].widget.attrs['placeholder'] = "Введите Фамилию"
        self.fields['first_name'].widget.attrs['placeholder'] = "Введите Имя"
        self.fields['email'].widget.attrs['placeholder'] = "Введите email"
        self.fields['image'].widget.attrs['placeholder'] = "Добавить фотографию"
        self.fields['age'].widget.attrs['placeholder'] = "Bозраст"

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['image'].widget.attrs['placeholder'] = "custom-file-input"


class UserAdminProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'last_name', 'first_name', 'email', 'image', 'age')

    def __init__(self, *args, **kwargs):
        super(UserAdminProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = True

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'
