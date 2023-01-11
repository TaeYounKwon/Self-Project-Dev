from geopy.geocoders import Nominatim
import requests, json

def current_location():
    here_req = requests.get("http://www.geoplugin.net/json.gp")

    if (here_req.status_code != 200):
        print("현재좌표를 불러올 수 없음")
    else:
        location = json.loads(here_req.text)
        crd = {"lat": str(location["geoplugin_latitude"]), "lng": str(location["geoplugin_longitude"])}

    return crd

def geocoding_reverse(lat_lng_str): 
    geolocoder = Nominatim(user_agent = 'South Korea', timeout=None)
    address = geolocoder.reverse(lat_lng_str)

    return address



crd = current_location()
lat = crd['lat']
lng = crd['lng']
location = lat+', '+lng
# 적도 위도의 값
print(location)

# 적도 위도의 값을 geocoding하여 한국의 위치를 알려줌!
address = geocoding_reverse(location)
print(address)