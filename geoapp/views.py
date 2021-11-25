from django.shortcuts import render

# Create your views here.
from geoapp.models import Measurement
from geoapp.forms import MeasurementForm


def calcutae_location(request, ):
    distance = Measurement.objects.get(id=1)
    form = MeasurementForm(request.POST or None)
    
    if form.is_valid():
        instance = form.save(commit=False)
        instance.destination = form.cleaned_data['destination']
        instance.loaction = 'Dhaka'
        instance.distance = 500
        instance.save()


    return render(request, 'measurements/main.html', {
        'distance':distance,
        'form':form
    })