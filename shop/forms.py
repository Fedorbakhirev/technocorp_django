from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

from shop.models import Order


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={
        'class': 'w-full sm:w-1/3 m-auto border border-x-gray focus:border-gray-400 focus:outline-none py-2 px-2',
        'autocomplete': 'off',
        'placeholder': 'Логин', }))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class': 'w-full sm:w-1/3 m-auto border border-x-gray focus:border-gray-400 focus:outline-none py-2 px-2',
        'autocomplete': 'off',
        'placeholder': 'Пароль', }))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={
        'class': 'w-full sm:w-1/3 m-auto border border-x-gray focus:border-gray-400 focus:outline-none py-2 px-2',
        'autocomplete': 'off',
        'placeholder': 'Повторите пароль', }))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={
        'class': 'w-full sm:w-1/3 m-auto border border-x-gray focus:border-gray-400 focus:outline-none py-2 px-2',
        'autocomplete': 'off',
        'placeholder': 'Имя', }))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={
        'class': 'w-full sm:w-1/3 m-auto border border-x-gray focus:border-gray-400 focus:outline-none py-2 px-2',
        'autocomplete': 'off',
        'placeholder': 'Фамилия', }))
    email = forms.EmailField(label='Эл. почта', widget=forms.TextInput(attrs={
        'class': 'w-full sm:w-1/3 m-auto border border-x-gray focus:border-gray-400 focus:outline-none py-2 px-2',
        'autocomplete': 'off',
        'placeholder': 'Эл. почта', }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'email')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'w-full sm:w-1/3 m-auto border border-x-gray focus:border-gray-400 focus:outline-none py-2 px-2'}),
            'password1': forms.PasswordInput(attrs={
                'class': 'w-full sm:w-1/3 m-auto border border-x-gray focus:border-gray-400 focus:outline-none py-2 px-2'}),
            'password2': forms.PasswordInput(attrs={
                'class': 'w-full sm:w-1/3 m-auto border border-x-gray focus:border-gray-400 focus:outline-none py-2 px-2'}),
            'first_name': forms.TextInput(attrs={
                'class': 'w-full sm:w-1/3 m-auto border border-x-gray focus:border-gray-400 focus:outline-none py-2 px-2'}),
            'last_name': forms.TextInput(attrs={
                'class': 'w-full sm:w-1/3 m-auto border border-x-gray focus:border-gray-400 focus:outline-none py-2 px-2'}),
            'email': forms.TextInput(attrs={
                'class': 'w-full sm:w-1/3 m-auto border border-x-gray focus:border-gray-400 focus:outline-none py-2 px-2'}),
        }


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={
        'class': 'w-full sm:w-1/3 m-auto border border-x-gray focus:border-gray-400 focus:outline-none py-2 px-2',
        'autocomplete': 'off',
        'placeholder': 'Логин', }))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class': 'w-full sm:w-1/3 m-auto border border-x-gray focus:border-gray-400 focus:outline-none py-2 px-2',
        'autocomplete': 'off',
        'placeholder': 'Пароль', }))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(self.request, username=username, password=password)
        if user is not None:  # to check whether user is available or not?
            # the password verified for the user
            if user.is_active == False:
                raise ValidationError("Ваша учетная запись не активирована администратором")
            else:
                return super(LoginUserForm, self).clean()
        else:
            # the authentication system was unable to verify the username and password
            raise ValidationError("Пожалуйста, проверьте правильность написания логина и пароля.")

    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'w-full sm:w-1/3 m-auto border border-x-gray focus:border-gray-400 focus:outline-none py-2 px-2'}),
            'password': forms.PasswordInput(attrs={
                'class': 'w-full sm:w-1/3 m-auto border border-x-gray focus:border-gray-400 focus:outline-none py-2 px-2'}),
        }



