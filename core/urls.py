from django.urls import path
from weather.views import WeatherView, WeatherGenerate, WeatherReset, WeatherEdit, WeatherDelete

urlpatterns = [
    path('', WeatherView.as_view(), name='Weather View'),
    path('generate', WeatherGenerate.as_view(), name='Weather Generate'),
    path('reset', WeatherReset.as_view(), name='Weather Reset'),
    path('edit/<weather_id>/', WeatherEdit.as_view(), name='Weather Edit'),
    path('delete', WeatherDelete.as_view(), name='Weather Delete')
]
