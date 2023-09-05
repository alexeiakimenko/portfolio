from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
    lst = list(range(6, 21))

    return render(request, 'generator/home.html', {'lst': lst})


def password(request):
    char = []
    char = [chr(i) for i in range(97, 123)]
    if request.GET.get('uppercase'):
        char.extend([chr(i) for i in range(65, 91)])
    if request.GET.get('numbers'):
        char.extend([chr(i) for i in range(48, 58)])
    if request.GET.get('special'):
        char.extend([chr(i) for i in range(33, 48)])

    lenght = int(request.GET.get('lenght'))
    psw = ''
    for i in range(lenght):
        psw += random.choice(char)

    return render(request, 'generator/password.html', {'password': psw})


def rules(request):
    return render(request, 'generator/rules.html')
