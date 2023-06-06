from django.shortcuts import render, redirect, HttpResponse
from .models import ChargingStation
from .forms import ChargingStationForm
# Create your views here.

def charging_station_map(request):
    if request.user.is_authenticated:
        charging_stations = ChargingStation.objects.all()
        context = {'charging_stations': charging_stations}
        return render(request, 'maps/charging_stations.html', context)
    else:
        return HttpResponse("<h1>Only authenticated user can access</h1>")

def register_charging_station(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ChargingStationForm(request.POST)
            print(form)
            if form.is_valid():
                form.save()
                return redirect('/')  # Redirect to the map page or any other desired URL
            else:
                return HttpResponse("Invalid")
        else:
            form = ChargingStationForm()
        return render(request, 'maps/register_charger.html', {'form': form})
    else:
        return HttpResponse("<h1>Only authenticated user can access</h1>")

def charger_details(request, id):
    charger = ChargingStation.objects.get(id=id)
    context = {'charger':charger}
    return render(request, 'maps/charger_details.html', context)

