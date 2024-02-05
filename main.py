from geopy.geocoders import Nominatim
from geopy import distance

geocoder = Nominatim(user_agent="distance")
location1 = "kandy"             #place 1
location2 = "nawalapitiya"      #place 2

coordinates1 = geocoder.geocode(location1)
coordinates2 = geocoder.geocode(location2)

lat1,long1 = (coordinates1.latitude),(coordinates1.longitude)
lat2,long2 = (coordinates2.latitude),(coordinates2.longitude)

place1 = (lat1,long1)
place2 = (lat2,long2)


print("Distance Between Two Places : ",distance.distance(place1,place2))