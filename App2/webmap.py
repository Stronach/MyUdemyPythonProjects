# webmap.py

import folium
import pandas
from geopy.geocoders import Nominatim
nom=Nominatim()

data=pandas.read_csv("listings.csv")
data["Address"] = data["ADDRESS"]+", "+ data["STATE"]+", "+ str(data["MAILING ZIPCODE"])

for n in data["Address"]:

    x=nom.geocode(data["Address"])
    x.latitude
    x.longitude

lat = list(data["LAT"])
lon = list(data["LON"])
map = folium.Map(location =[43,-75], zoom_start=5, tiles="Mapbox Bright")
fg = folium.FeatureGroup(name="My Map")


for lt, ln in zip(lat,lon):
    fg.add_child(folium.Marker(location = [lt,ln], popup="""<h3>This is a popup<h3>""", icon=folium.Icon('green')))
map.add_child(fg)

map.save("Map1.html")
