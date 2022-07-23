from django.urls import path
from . import views

urlpatterns = [

    # Main url
    path('Home/', views.home, name='home'),

    # access these urls only if the actual data source has updated any data
    # these urls fetch all the data from the actual source
    path('getCountries/', views.countries, name='getcountries'),
    path('getStates/', views.states, name='getstates'),
    path('getCities/', views.cities, name='getcities')
]