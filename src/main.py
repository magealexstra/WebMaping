import folium
import pandas as pd

with open("DATA\\Volcanoes.txt", "r") as volc:
    V_lst = pd.read_csv(volc, header=0)


names = V_lst["NAME"]
lat = list(V_lst["LAT"])
lon = list(V_lst["LON"])
elv = list(V_lst["ELEV"])

m = folium.Map(location=[47.1954, -120.9392], zoom_start=7, tiles="Stamen Terrain", control_scale=True)

fg = folium.FeatureGroup(name="Overlay")

for lt, ln, nms, ev in zip(lat, lon, names, elv):
    color = ""
    e = int(ev)
    if e <= 1000:
        color = "green"
    elif e >= 3000:
        color = "red"
    else:
        color = "orange"
    fg.add_child(folium.Marker(location=[lt, ln], popup=f"{nms, ev}", icon=folium.Icon(color=f"{color}")))

m.add_child(fg)

m.save("DATA\\firstmap.html")
