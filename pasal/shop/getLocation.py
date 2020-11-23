import geocoder
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="user",timeout=10)


def send_loc(request):
    g = geocoder.ip('me')
    return g
