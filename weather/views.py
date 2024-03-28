from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import WeatherForm
from .repositories import WeatherRepository
from .serializers import WeatherSerializer

class WeatherView(View):
    def get(self, request):
        repository = WeatherRepository(collectionName='weathers')
        weathers = repository.getAll()  # Obter todos os dados do clima do banco de dados
        weather_with_ids = []  # Lista para armazenar os dados do clima com seus IDs

        for index, weather in enumerate(weathers):
            # Converter o objeto MongoDB em um dicionário Python
            weather_dict = {
                'temperature': weather['temperature'],
                'date': weather['date'],
                'city': weather.get('city', ''),
                'atmosphericPressure': weather.get('atmosphericPressure', ''),
                'humidity': weather.get('humidity', ''),
                'weather': weather.get('weather', '')
            }
            weather_with_ids.append((str(index), weather_dict))  # Adicionar o clima à lista

        return render(request, "home.html", {"weathers": weather_with_ids})




class WeatherGenerate(View):
    def get(self, request):
        form = WeatherForm()
        return render(request, "generate_weather.html", {'form': form})

    def post(self, request):
        form = WeatherForm(request.POST)
        if form.is_valid():
            repository = WeatherRepository(collectionName='weathers')
            weather = {
                'temperature': form.cleaned_data['temperature'],
                'date': form.cleaned_data['date'],
                'city': form.cleaned_data['city'],
                'atmosphericPressure': form.cleaned_data['atmosphericPressure'],
                'humidity': form.cleaned_data['humidity'],
                'weather': form.cleaned_data['weather'],
            }
            serializer = WeatherSerializer(data=weather)
            if serializer.is_valid():
                repository.insert(serializer.validated_data)
                return redirect('Weather View')
            else:
                errors = serializer.errors
                return HttpResponse(f"Erros de validação: {errors}", status=400)
        return render(request, "generate_weather.html", {'form': form})
    
class WeatherEdit(View):
    def get(self, request, weather_id):
        repository = WeatherRepository(collectionName='weathers')
        weather = repository.getById(weather_id)
        form = WeatherForm(initial=weather)
        return render(request, "edit_weather.html", {'form': form, 'weather_id': weather_id})


    def post(self, request, weather_id):
        form = WeatherForm(request.POST)
        if form.is_valid():
            repository = WeatherRepository(collectionName='weathers')
            weather_data = {
                'temperature': form.cleaned_data['temperature'],
                'date': form.cleaned_data['date'],
                'city': form.cleaned_data['city'],
                'atmosphericPressure': form.cleaned_data['atmosphericPressure'],
                'humidity': form.cleaned_data['humidity'],
                'weather': form.cleaned_data['weather'],
            }
            repository.update(weather_id, weather_data)
            return redirect('Weather View')
        return render(request, "generate_weather.html", {'form': form, 'weather_id': weather_id})


class WeatherDelete(View):
    def post(self, request, weather_id):
        repository = WeatherRepository(collectionName='weathers')
        repository.delete(weather_id)
        return redirect('Weather View')

    
class WeatherReset(View):
    def get(self, request):
        repository = WeatherRepository(collectionName='weathers')
        repository.deleteAll()
        return redirect('Weather View')