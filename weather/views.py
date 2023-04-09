import requests
from django.shortcuts import render

from .models import City
from .forms import CityForm


def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=97332dbd9c9a54e175781b9b8b53364e'
    city = 'London'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
        # print(request.POST)

    form = CityForm()

    cities = City.objects.all()
    weather_data = []
    for city in cities:
        r = requests.get(url.format(city)).json()
        # print(r.text)

        city_weather = {
            'city': city.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }
        weather_data.append(city_weather)
    # print(weather_data)
    # print(city_weather)
    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'weather/weather.html', context)
