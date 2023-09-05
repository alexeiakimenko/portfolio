from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import City


# Create your views here.
@login_required
def attraction(request):
    project = City.objects.all()
    return render(request, 'city/attraction.html', {'projects': project})


def index(request):
    return render(request, 'city/index.html')


def register(request):
    if request.method == 'GET':
        return render(request, 'city/register.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('attraction')
            except IntegrityError:
                return render(request, 'city/register.html',
                              {'form': UserCreationForm(),
                               'error': 'Такое имя пользователя существует,создайте другое!'})


        else:
            return render(request, 'city/register.html',
                          {'form': UserCreationForm(), 'error': 'Пароли не совпадают!'})


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'city/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'city/loginuser.html', {'form': AuthenticationForm(),
                                                           'error': 'Неверные данные для входа'})
        else:
            login(request, user)
            return redirect('attraction')
