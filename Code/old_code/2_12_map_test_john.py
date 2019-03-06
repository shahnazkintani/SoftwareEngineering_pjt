'''
Change_log:
2/11/2019:
Put map_test.py and 40_dp_test.csv file under same file and open the map_john.html to see the result.
2/12/2019:
Now put go_track_trackspoints.csv file under same file and open the map_john.html to see the result; Limit the number of points in for loop can in crease the efficiency.

'''
# Wabbits needed
import folium
import pandas as pd

# read data from csv file and map name
data_name = pd.read_csv("go_track_trackspoints.csv")
save_name = 'map_john.html'

#basic data information
print(data_name.columns)
print(data_name.dtypes)

# use panda to frame data
dataframed_data = pd.DataFrame(data_name)

#A list of avaliable colors
color_set = ['red', 'blue', 'green', 'purple', 'orange', 'darkred',
             'lightred', 'beige', 'darkblue', 'darkgreen', 'cadetblue',
             'darkpurple', 'pink', 'lightblue', 'lightgreen',
             'gray', 'black', 'lightgray']
color_code = 0

#Map starts here
m = folium.Map(location=[-10.93934139, -37.06274211], tiles='Stamen Toner', zoom_start=10)

#Color change function
def changeColor():
	global color_code
	if color_code+1 >= len(color_set):
		color_code = 0
	color_code = color_code + 1

#dataframed['id'] = dataframed['id'].astype(object)
#print(data.dtypes)

#Plot all the data in the csv file MINUS 15000 for efficiency (MARKED FOR DEBUG)
for i in range(1,len(dataframed_data)-15000):
	#change color upon change track_id
	if (dataframed_data.iloc[i-1]['track_id'] != dataframed_data.iloc[i]['track_id']):
		changeColor()
		folium.Marker([dataframed_data.iloc[i]['latitude'], dataframed_data.iloc[i]['longitude']], popup = dataframed_data.iloc[i]['time'], icon = folium.Icon(color=color_set[color_code])).add_to(m) 
	else:
		folium.Marker([dataframed_data.iloc[i]['latitude'], dataframed_data.iloc[i]['longitude']], popup = dataframed_data.iloc[i]['time'], icon = folium.Icon(color=color_set[color_code])).add_to(m)

#save map to current directory
print("Map created, save to:", save_name)
m.save(save_name)


'''
['red', 'blue', 'green', 'purple', 'orange', 'darkred',
             'lightred', 'beige', 'darkblue', 'darkgreen', 'cadetblue',
             'darkpurple', 'white', 'pink', 'lightblue', 'lightgreen',
             'gray', 'black', 'lightgray']

DEBUG LOG:

1. for loop will ignore very first data point, since it starts from 1.
'''
