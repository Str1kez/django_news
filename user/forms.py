from captcha.fields import CaptchaField
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

large_box = 'col-12 py-3 form-control fh5co_contact_text_box'
# small_box = 'col-6 py-3 form-control fh5co_contact_text_box'


class CreateUserForm(UserCreationForm):
    username = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': large_box}),
                               label='Имя')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': large_box}),
                             label='Email')
    password1 = forms.CharField(required=True,
                                widget=forms.PasswordInput(attrs={'class': large_box}),
                                label='Пароль')
    password2 = forms.CharField(required=True,
                                widget=forms.PasswordInput(attrs={'class': large_box}),
                                label='Повторите пароль')
    captcha = CaptchaField(label='')

    class Meta:
        model = User
        fields = 'username', 'password1', 'password2', 'email'


class AuthUserForm(AuthenticationForm):
    username = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': large_box}),
                               label='Имя')
    password = forms.CharField(required=True,
                               widget=forms.PasswordInput(attrs={'class': large_box}),
                               label='Пароль')
    captcha = CaptchaField(label='', )
