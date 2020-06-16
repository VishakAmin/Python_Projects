import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lot = list(data["LON"])
elev = list(data["ELEV"])

def color_prducer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation <3000:
        return 'orange'
    else:
        return 'red'        


map = folium.Map(location = [38.58, -99.09], zoom_start = 6,tiles = "Stamen Terrain")

fgv = folium.FeatureGroup(name = "Volcanoes")

for la, lo, el in zip(lat, lot, elev):
    fgv.add_child(folium.CircleMarker(location = [la,lo], radius  = 6 ,popup=folium.Popup(str(el),parse_html=True) , fill_color=color_prducer(el), color = 'grey', fill_opacity = 0.7 ))

fgp = folium.FeatureGroup(name = "Population")
fgp.add_child(folium.GeoJson(data = open('world.json','r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']<10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] <20000000 else 'red'}))


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")






