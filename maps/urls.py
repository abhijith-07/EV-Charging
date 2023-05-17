from . import views
from django.urls import path

app_name = 'maps'
urlpatterns = [
    path('', views.charging_station_map, name='chargingStations'),
    path('register/', views.register_charging_station, name='register_charging_station')
]
