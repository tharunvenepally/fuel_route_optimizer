import requests
from django.conf import settings

MAPQUEST_BASE_URL = "http://www.mapquestapi.com/directions/v2/route"

def get_route(start_location, end_location):
    params = {
        'key': settings.MAPQUEST_API_KEY,
        'from': start_location,
        'to': end_location,
        'unit': 'm'
    }
    
    response = requests.get(MAPQUEST_BASE_URL, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Unable to fetch route from MapQuest"}
