from django import forms
from .models import ChargingStation
from leaflet.forms.widgets import LeafletWidget

class ChargingStationForm(forms.ModelForm):
    class Meta:
        model = ChargingStation
        fields = ['name', 'latitude', 'longitude']
        widgets = {
            'latitude': LeafletWidget(),
            'longitude': LeafletWidget(),
        }
