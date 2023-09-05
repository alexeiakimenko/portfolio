from django.shortcuts import render, redirect, get_object_or_404
import requests
from .models import *
from .forms import *


# Create your views here.
def weather(request):
    app_id = '2d9cfe7919e74b4386e40250233108'
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
    form = CityForm()
    cities = City.objects.all()
    all_cities = []
    for city in cities:
        url = f"http://api.weatherapi.com/v1/current.json?key={app_id}&q={city.name}&aqi=no"
        res = requests.get(url).json()
        try:
            city_info = {
                'city_pk': city.id,
                'city': city,
                'temp': res['current']['temp_c'],
                'wind': res['current']['wind_kph'],
                'icon': res['current']['condition']['icon']
            }
        except KeyError:
            city_info = {
                'city_pk': city.id,
                'city': city,
                'temp': '-',

            }
        all_cities.append(city_info)
    context = {
        'all_info': all_cities,
        'form': form,
    }

    return render(request, 'weather/weather.html', context)


def deletecity(request, city_pk):
    city = get_object_or_404(City, pk=city_pk)
    if request.method == 'POST':
        city.delete()
        return redirect('weather')
