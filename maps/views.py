from django.shortcuts import render, redirect
from .models import ChargingStation
from .forms import ChargingStationForm
# Create your views here.

def charging_station_map(request):
    charging_stations = ChargingStation.objects.all()
    context = {'charging_stations': charging_stations}
    return render(request, 'maps/charging_stations.html', context)

def register_charging_station(request):
    if request.method == 'POST':
        form = ChargingStationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirect to the map page or any other desired URL
    else:
        form = ChargingStationForm()
    return render(request, 'maps/register_charger.html', {'form': form})

