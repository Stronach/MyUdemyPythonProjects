import folium
import pandas
from geopy.geocoders import Nominatim
nom=Nominatim()

def eval_results(x):
    try:
        data["LAT"]=x.latitude
        data["LON"]=x.longitude
        return x.latitude, x.longitude
    except:
        #data["Address"] = data["ADDRESS"]+", "+ data["MAILING ZIPCODE"] +", "+ data["STATE"]
        #data["Cordinates"]=data["Address"].apply(nom.geocode).apply(lambda x: eval_results(x))
        return (40, -75)

data=pandas.read_csv("listings.csv", dtype={'MAILING ZIPCODE': 'str'})
data["Address"] = data["ADDRESS"]+", "+ data["MAILING ZIPCODE"]

data["Cordinates"]=data["Address"].apply(nom.geocode).apply(lambda x: eval_results(x))
n=data.Cordinates
lat=list(data["LAT"])
lon=list(data["LON"])

listing=list(data["TYPE"])
print(listing)
fg = folium.FeatureGroup(name="My Map")
print(n)
map = folium.Map(location =[43,-75], zoom_start=7)
#for cor in data.Cordinates:
#    if cor is "(None, None)":
#        data["Address"] = data["ADDRESS"]+", "+ data["MAILING ZIPCODE"] +", "+ data["STATE"]
#        data["Cordinates"]=data["Address"].apply(nom.geocode).apply(lambda x: eval_results(x))
#    print(data["Cordinates"])

for lt, ln, lis in zip(lat,lon,listing):
    fg.add_child(folium.Marker(location = [lt,ln], popup=lis, icon=folium.Icon(color='green')))

#lat = list(data["LAT"])
#lon = list(data["LON"])
# map = folium.Map(location =[43,-75], zoom_start=10)
#fg = folium.FeatureGroup(name="My Map")
map.add_child(fg)

map.save("Map1.html")
