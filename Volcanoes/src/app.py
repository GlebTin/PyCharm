import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])

def color_production(elevator):
    if elevator < 1000:
        return "green"
    elif 1000 <= elevator < 2500:
        return "gray"
    else:
        return "red"


map = folium.Map(location=[35.55, -99.09], zoom_start=5, title='')

fgv = folium.FeatureGroup(name='Volcanoes')

for lt, ln, lv in zip(lat, lon, elev):
    #fgv.add_child(folium.Marker(location=[lt, ln], popup=str(lv) + ' m.', radius=6, icon=folium.Icon(color=color_production(lv))))
    fgv.add_child(folium.CircleMarker(location=[lt, ln], popup=str(lv) + 'm', radius=6,
                               fill_color=color_production(lv), color='gray', fill_opacity=0.7))

fgp = folium.FeatureGroup(name='Population')
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                             style_function=lambda x: {'fillColour': 'green' if x['properties']['POP2005'] < 1000000
                             else 'orange' if 1000000 <= x['properties']['POP2005'] < 2000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
folium.LayerControl().add_to(map)
map.save('map.html')

