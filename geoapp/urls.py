from django.urls import path


from geoapp.views import *


urlpatterns = [
    path('', calcutae_location, name='calculate_location'),
]