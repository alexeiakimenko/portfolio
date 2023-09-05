<<<<<<< HEAD
from django.shortcuts import render
import requests


# Create your views here.
def exchange(request):
    response = requests.get(url='https://api.exchangerate.host/lastest').json()
    currencies = response.get('rates')
    if request.method == 'GET':
        context = {
            'currencies': currencies
        }
        return render(request, 'exchange/index.html', context)
    if request.method == 'POST':
        from_amount = request.POST.get('from-amount')
        from_curr = request.POST.get('from-curr')
        to_curr = request.POST.get('to-curr')
        converted_amount = round(currencies[to_curr] / currencies[from_curr] * float(from_amount), 2)
        context = {
            'from_curr': from_curr,
            'to_curr': to_curr,
            'currencies': currencies,
            'converted_amount': converted_amount,
            'from_amount': from_amount,
        }
        return render(request, 'exchange/index.html', context)
=======
from django.shortcuts import render
import requests


# Create your views here.
def exchange(request):
    response = requests.get(url='https://api.exchangerate.host/lastest').json()
    currencies = response.get('rates')
    if request.method == 'GET':
        context = {
            'currencies': currencies
        }
        return render(request, 'exchange/index.html', context)
    if request.method == 'POST':
        from_amount = request.POST.get('from-amount')
        from_curr = request.POST.get('from-curr')
        to_curr = request.POST.get('to-curr')
        converted_amount = round(currencies[to_curr] / currencies[from_curr] * float(from_amount), 2)
        context = {
            'from_curr': from_curr,
            'to_curr': to_curr,
            'currencies': currencies,
            'converted_amount': converted_amount,
            'from_amount': from_amount,
        }
        return render(request, 'exchange/index.html', context)
>>>>>>> c56e1a6cee1fb286d87fdf677c9758e9a101d523
