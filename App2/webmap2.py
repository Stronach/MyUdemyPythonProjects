import folium
import pandas
from geopy.geocoders import Nominatim
nom=Nominatim()

def eval_results(x):
    try:
        return (x.latitude, x.longitude)
    except:
        return (None, None)

data=pandas.read_csv("listings.csv", dtype={'MAILING ZIPCODE': 'str'})
data["Address"] = data["ADDRESS"]+", "+ data["MAILING ZIPCODE"]

data["Cordinates"]=data["Address"].apply(nom.geocode).apply(lambda x: eval_results(x))
n=data.Cordinates


listing=str(data["TYPE"])
print(listing)
fg = folium.FeatureGroup(name="My Map")
print(n)
map = folium.Map(location =[43,-75], zoom_start=7)
for lt in n:
    if data.Cordinates is "None":
        data["Address"] = data["ADDRESS"]+", "+ data["MAILING ZIPCODE"] +", "+ data["STATE"]
        data["Cordinates"]=data["Address"].apply(nom.geocode).apply(lambda x: eval_results(x))
        #print(data["LAT"])
#    for lt, ln in zip(lat,lon):
    fg.add_child(folium.Marker(location = list(data.Cordinates), popup="""listing """+list(str(listings), icon=folium.Icon('green')))

#lat = list(data["LAT"])
#lon = list(data["LON"])
# map = folium.Map(location =[43,-75], zoom_start=10)
#fg = folium.FeatureGroup(name="My Map")
map.add_child(fg)

map.save("Map1.html")
