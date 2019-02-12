'''
Put map_test.py and 40_dp_test.csv file under same file and open the map_john.html to see the result
'''
import folium
import pandas as pd

# read data from csv file
data = pd.read_csv("40_dp_test.csv")
print(data.columns)
print(data.dtypes)

dataframed = pd.DataFrame(data)
print("dataframe success")

colorSet = ['red','green', 'blue','orange']
colorCode = 0
m = folium.Map(location=[-10.93934139, -37.06274211], tiles='Stamen Toner', zoom_start=10)

def changeColor():
	global colorCode
	colorCode = colorCode+1

#dataframed['id'] = dataframed['id'].astype(object)
#print(data.dtypes)

for i in range(1,len(dataframed)):
	if (dataframed.iloc[i-1]['track_id'] != dataframed.iloc[i]['track_id']):
		changeColor()
		folium.Marker([dataframed.iloc[i]['latitude'], dataframed.iloc[i]['longitude']], icon = folium.Icon(color=colorSet[colorCode])).add_to(m) 
	else:
		folium.Marker([dataframed.iloc[i]['latitude'], dataframed.iloc[i]['longitude']], popup = dataframed.iloc[i]['time'],icon = folium.Icon(color=colorSet[colorCode])).add_to(m) 

m.save('map_john.html')


'''
['red', 'blue', 'green', 'purple', 'orange', 'darkred',
             'lightred', 'beige', 'darkblue', 'darkgreen', 'cadetblue',
             'darkpurple', 'white', 'pink', 'lightblue', 'lightgreen',
             'gray', 'black', 'lightgray']
'''
