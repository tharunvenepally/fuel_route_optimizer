from django.urls import path
from .views import api_status, get_route_view
from .views import get_fuel_data, get_route_with_fuel_stops

urlpatterns = [
    # My testing API endpoints to test that each modules was working correctly before intergrating them together
    path('api/', api_status),
    path('api/route/', get_route_view),
    path('api/fuel-data/', get_fuel_data),

    # My final endpoint
    path('api/route_with_fuel_stops/', get_route_with_fuel_stops, name='route_with_fuel_stops'),
]
