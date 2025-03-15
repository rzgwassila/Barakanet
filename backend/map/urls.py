from django.urls import path
from django.shortcuts import render
from .views import  get_nearby_restaurants

def map_view(request):
    return render(request, "map.html")  # Make sure map.html is in your templates folder

urlpatterns = [
    path("api/nearby-restaurants/", get_nearby_restaurants, name="nearby_restaurants"),
#path('api/get_nearby_restaurants/', get_nearby_restaurants, name='get_nearby_restaurants'),
    path("map/", map_view, name="map"),  # Add this line
]
