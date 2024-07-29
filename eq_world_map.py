from pathlib import Path
import json
import plotly.express as px

path = Path('eq_data/2024_july.geojson')
contents = path.read_text()
all_eq_data = json.loads(contents)


all_eq_dicts = all_eq_data['features']
mags, lons, lats, eq_titles = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    eq_titles.append(eq_dict['properties']['title'])
title = 'Global Earthquakes in 2024 July'
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title,
                     color=mags,
                     color_continuous_scale='tempo',
                     labels={"color": "Magnitude"}, 
                     projection='robinson',
                     hover_name= eq_titles,
                     )
fig.show()
