from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .services.mapquest import get_route
from .utils.fuel_data import load_fuel_data, find_nearby_stops
from django.core.cache import cache
from django.conf import settings
import os

@api_view(['GET'])
def api_status(request):
    return Response({"status": "API is working"})

@api_view(['GET'])
def get_route_view(request):
    start_location = request.GET.get('start')
    end_location = request.GET.get('end')
    
    if not start_location or not end_location:
        return Response({"error": "Please provide both start and end locations."}, status=400)

    route_data = get_route(start_location, end_location)
    
    return Response(route_data)


FUEL_DATA_PATH = os.path.join(settings.BASE_DIR, 'data', 'fuel-prices-for-be-assessment.csv')

@api_view(['GET'])
def get_fuel_data(request):
    fuel_data = load_fuel_data(FUEL_DATA_PATH)
    
    if fuel_data is None:
        return Response({"error": "Failed to load fuel data"}, status=500)
    return Response(fuel_data.head(5).to_dict(orient='records'))

@api_view(['GET'])
def get_route_with_fuel_stops(request):
    """
    API to return the route data with optimal fuel stops along the route.
    """
    start_location = request.GET.get('start')
    end_location = request.GET.get('end')
    
    if not start_location or not end_location:
        return Response({"error": "Please provide both start and end locations."}, status=400)

    cache_key = f"route_{start_location}_{end_location}"

    route_data = cache.get(cache_key)

    if not route_data:
        route_data = get_route(start_location, end_location)
    
        if 'error' in route_data:
            return Response(route_data, status=500)
        cache.set(cache_key, route_data, timeout=60*60*24)

    fuel_data = load_fuel_data(FUEL_DATA_PATH)
    
    if fuel_data is None:
        return Response({"error": "Failed to load fuel data"}, status=500)
    
    total_fuel_cost = 0
    fuel_stops = []

    vehicle_range = 500
    miles_per_gallon = 10

    maneuvers = route_data['route']['legs'][0]['maneuvers']

    for maneuver in maneuvers:
        start_point = maneuver['startPoint']

        nearby_stops = find_nearby_stops(fuel_data, start_point['lat'], start_point['lng'], max_distance=vehicle_range)

        if not nearby_stops.empty:
            cheapest_stop = nearby_stops.loc[nearby_stops['Retail Price'].idxmin()]
            fuel_stops.append({
                "truckstop_name": cheapest_stop['Truckstop Name'],
                "address": cheapest_stop['Address'],
                "city": cheapest_stop['City'],
                "state": cheapest_stop['State'],
                "fuel_price": cheapest_stop['Retail Price'],
                "distance_from_route": cheapest_stop['distance']
            })

            distance = maneuver['distance']  
            gallons_needed = distance / miles_per_gallon
            total_fuel_cost += gallons_needed * cheapest_stop['Retail Price']

    return Response({
        "route": route_data['route'],
        "fuel_stops": fuel_stops,
        "total_fuel_cost": total_fuel_cost
    })
