import folium
import pandas

data= pandas.read_csv("volcanoes.csv")
elev = list(data["ELEV"])

lat=data["LAT"]
lon=data["LON"]
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[38.58,-99.09], zoom_start=5, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location=[lt,ln], color=color_producer(el), fill=True, fill_opacity=.8, fill_color=color_producer(el), popup=str(el)+" m" , icon=folium.Icon(color=color_producer(el))))

fg.add_child(folium.GeoJson(data = open('world.json', encoding='utf-8-sig').read(),
style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange'
if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))
map.add_child(fg)

map.save("Map.html")
