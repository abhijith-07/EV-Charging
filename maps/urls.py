from . import views
from django.urls import path

app_name = 'maps'
urlpatterns = [
    path('', views.chargingStations, name='chargingStations'),
]
