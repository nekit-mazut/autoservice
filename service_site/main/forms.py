from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from django.core.validators import EmailValidator, RegexValidator

from .models import CustomUser


class ClientRegister(UserCreationForm):
    username = forms.CharField(label="Логин ", widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email ', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль ', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля ', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = CustomUser
        fields = ["username", "email", "password1", "password2"]


class AuthenticationForm1(AuthenticationForm):
    username = forms.CharField(label="Логин ",
                               widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Введите логин'}))
    password = forms.CharField(label='Пароль ',
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-input', 'placeholder': 'Введите пароль'}))


class UserProfileForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'phone_number', 'first_name', 'last_name']

    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-input'}),
        validators=[EmailValidator(message='Введите корректный адрес электронной почты.')]
    )

    phone_number = forms.CharField(
        label='Номер телефона',
        widget=forms.TextInput(attrs={'class': 'form-input'}),
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message='Введите корректный номер телефона (от 9 до 15 цифр).'
            )
        ]
    )
