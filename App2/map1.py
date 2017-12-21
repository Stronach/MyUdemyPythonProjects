import folium
import pandas


data= pandas.read_csv("volcanoes.csv")

lat=data["LAT"]
lon=data["LON"]

map = folium.Map(location=[38.58,-99.09], zoom_start=6, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="My Map")

for lt, ln in zip(lat, lon):
    fg.add_child(folium.Marker(location=[lt,ln], popup="""<h3>Pop up marker</h3>""", icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map.html")
