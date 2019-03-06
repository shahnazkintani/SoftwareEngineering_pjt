import geopandas as gpd 
from shapely.geometry import Polygon
import pandas as pd 
import csv 

# read data from csv file
data = pd.read_csv("40_dp_test.csv")
print (data.columns)
print (data.dtypes)

dataframed = pd.DataFrame(data)
print('dataframe success')

#  To check the values in the csv file.
with open('40_dp_test.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        print(row)

csvFile.close()

# convert the colums from csv file to lat/long list.
data = pd.read_csv('40_dp_test.csv')
col_lat = list(data.latitude)
col_long = list(data.longitude)
# print (col_lat[0])

col_lat.append(col_lat[0])
col_long.append(col_long[0])
print (col_lat)
print (col_long)


col_lat = [-10.93934139, -10.93932395, -10.93921056, -10.93934139 ]
col_long= [-37.06274211, -37.06276451, -37.06284305, -37.06274211 ]

# polygon_geom = Polygon(zip(lon_point_list, lat_point_list))
polygon_geom = Polygon(zip(col_lat, col_long))
crs = {'init': 'epsg:4326'}
polygon = gpd.GeoDataFrame(index=[0], crs=crs, geometry=[polygon_geom])
print(polygon.geometry)

polygon.to_file(filename='polygon.geojson', driver ='GeoJSON')
polygon.to_file(filename='polygon.shp', driver ='ESRI Shapefile')

import folium
# m = folium.Map([50.854457, 4.377184], zoom_start=5, tiles='cartodbpositron')

# code migrated from CodeJohn2.py
colorSet = ['red','green', 'blue','orange']
colorCode = 0
m = folium.Map(location=[-10.93934139, -37.06274211], zoom_start=10)

def changeColor():
	global colorCode
	colorCode = colorCode+1

# for marker (test)
for i in range(1,len(dataframed)):
	if (dataframed.iloc[i-1]['track_id'] != dataframed.iloc[i]['track_id']):
		changeColor()
		folium.Marker([dataframed.iloc[i]['latitude'], dataframed.iloc[i]['longitude']], icon = folium.Icon(color=colorSet[colorCode])).add_to(m) 
	else:
		folium.Marker([dataframed.iloc[i]['latitude'], dataframed.iloc[i]['longitude']], popup = dataframed.iloc[i]['time'],icon = folium.Icon(color=colorSet[colorCode])).add_to(m) 



folium.GeoJson(polygon).add_to(m)
folium.LatLngPopup().add_to(m)

m.save('polygon_Prawan.html')