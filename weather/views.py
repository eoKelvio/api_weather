import datetime
from random import randrange
from django.views import View
from django.shortcuts import redirect, render
from .repositories import WeatherRepository
from weather.models import WeatherEntity

class WeatherView(View):
   
    def get(self, request):
        repository = WeatherRepository(collectionName='weathers')
        weathers = repository.getAll()
        return render(request, "home.html", {"weathers":weathers})
    

class WeatherGenerate(View):
    def get(self, request):
        repository = WeatherRepository(collectionName='weathers')
        # wheater = WeatherEntity(
        #     temperature=randrange(start=17, stop=40),
        #     date=datetime.now()
        # )
        wheater = {
            "temperature" : 28,
            "date": "hoje"
            }
        repository.insert(wheater)

        return redirect('Weather View')