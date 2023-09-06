from django.contrib.auth.forms import AuthenticationForm
from users.models import User
from django import forms


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Введите имя пользователя'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control py-4'

    class Meta:
        model = User
        fields = ('username', 'password', 'password')
