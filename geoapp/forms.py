from django import forms
from django.forms import fields

from geoapp.models import Measurement


class MeasurementForm(forms.ModelForm):
    class Meta:
        model = Measurement
        fields = ('destination', )
        