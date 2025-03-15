import requests
from django.http import JsonResponse

# API URLs
OVERPASS_API_URL = "https://overpass-api.de/api/interpreter"
OSM_API_URL = "https://nominatim.openstreetmap.org/search"

# Headers for OSM API
HEADERS = {
    "User-Agent": "MyDjangoApp/1.0 (contact@example.com)"  # Replace with your email
}

def get_nearby_restaurants(request):
    lat = request.GET.get("lat")
    lon = request.GET.get("lon")

    if not lat or not lon:
        return JsonResponse({"error": "Latitude and longitude are required"}, status=400)

    all_restaurants = []

    # ✅ 1. Fetch from Overpass API (structured data)
    overpass_query = f"""
    [out:json];
    (
      node["amenity"="restaurant"](around:2000,{lat},{lon});
      node["amenity"="cafe"](around:2000,{lat},{lon});
      node["amenity"="fast_food"](around:2000,{lat},{lon});
      node["amenity"="food_court"](around:2000,{lat},{lon});
    );
    out body;
    """
    
    overpass_response = requests.get(OVERPASS_API_URL, params={"data": overpass_query})

    if overpass_response.status_code == 200:
        overpass_data = overpass_response.json()
        overpass_restaurants = [
            {
                "name": element.get("tags", {}).get("name", "Unknown Restaurant"),
                "latitude": element["lat"],
                "longitude": element["lon"],
                "type": element.get("tags", {}).get("amenity", "Unknown Type"),
                "source": "Overpass API"
            }
            for element in overpass_data.get("elements", [])
        ]
        all_restaurants.extend(overpass_restaurants)

    # ✅ 2. Fetch from Nominatim API (keyword search)
    search_keywords = [
        "restaurant", "cafe", "food", "fast food", "dining", "eatery", "bistro",
        "pizzeria", "burger", "grill", "buffet", "diner", "Mata3im El Rahma"
    ]

    for keyword in search_keywords:
        params = {
            "q": keyword,
            "format": "json",
            "limit": 20,
            "bounded": 1,
            "viewbox": f"{float(lon)-0.1},{float(lat)+0.1},{float(lon)+0.1},{float(lat)-0.1}"
        }

        osm_response = requests.get(OSM_API_URL, params=params, headers=HEADERS)

        if osm_response.status_code == 200:
            osm_data = osm_response.json()
            osm_restaurants = [
                {
                    "name": place.get("display_name"),
                    "latitude": float(place.get("lat")),
                    "longitude": float(place.get("lon")),
                    "type": keyword,
                    "source": "Nominatim API"
                }
                for place in osm_data
            ]
            all_restaurants.extend(osm_restaurants)

    return JsonResponse({"restaurants": all_restaurants})
