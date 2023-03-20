from django.shortcuts import render

# Create your views here.

def chargingStations(request):
    markers_data = [
        {'lat': 8.5678, 'lng': 76.8908, 'popup': 'Karyavattom'},
        {'lat': 8.5678, 'lng': 76.8908, 'popup': 'Karyavattom'}
    ]
    context = {'markers': markers_data}
    return render(request, 'maps/charging_stations.html', context)