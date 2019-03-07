'''
Change_log:
2/11/2019:
Put map_test.py and 40_dp_test.csv file under same file and open the map_john.html to see the result.
2/12/2019:
Now put go_track_trackspoints.csv file under same file and open the map_john.html to see the result; Limit the number of points in for loop can in crease the efficiency.
2/18/2019: 
Add in control flow to control the map creation and Data description
2/25/2019:
Clean up the code and package the functions, Add in control flow to control the point/line plot and heatmap creation
'''
# Libraries & global values:
import folium
from folium import plugins
import pandas as pd

#Initialize colors
color_set = ['red', 'blue', 'green', 'purple', 'orange', 'darkred',
				'lightred', 'beige', 'darkblue', 'darkgreen', 'cadetblue',
				'darkpurple', 'pink', 'lightblue', 'lightgreen',
				'gray', 'black', 'lightgray']
color_code = 0

def display_Data_Info(data_name):
	decision_1 = input("Do yo uwant to display basic Data information? (y/n):")
	if decision_1 == 'y':
		print(data_name.columns)
		print(data_name.dtypes)
	else:
		print("Skip basic data info...")
		
def specify_map_attr():
	global DEF_LAT, DEF_LON
	decision_2 = input("Do yo uwant to Do you want to specify map position? (y/n):")
	if decision_2 == 'y':
		DEF_LON = eval(input("Starting longitude: "))
		DEF_LAT = eval(input("Starting latitude: "))
		#setting map creation attribute
	else:
		print("Using Default Longitude and Latitude...")

def creat_map(DEF_LON,DEF_LAT):
	#Map starts here
	print("Starting Basic Layer Creation...")
	return folium.Map(location=[DEF_LAT, DEF_LON], tiles='Stamen Toner', zoom_start=10)

def change_color(color_set):
	#Color change function
	global color_code
	#print(color_code)
	if color_code + 1 >= len(color_set):
		color_code = 0
	color_code = color_code + 1

#Plot point onto the map for selected group 
def plot_marker(temp_trackID, color_code, color_set, m):
	### (MARKED FOR DEBUG IN FOR STARTING LOOP RANGE)
	for i in range(1, len(temp_trackID)):
		folium.Marker([temp_trackID.iloc[i]['latitude'], temp_trackID.iloc[i]['longitude']], popup = temp_trackID.iloc[i]['time'], icon = folium.Icon(color=color_set[color_code])).add_to(m)

def plot_line(temp_tuple, color_code, color_set, m):
	folium.PolyLine(temp_tuple, color=color_set[color_code], weight=2.5, opacity=1).add_to(m)

def heatmap(temp_trackID, m):
	# convert to (n, 2) nd-array format for heatmap
	stationArr = temp_trackID[['latitude', 'longitude']].values
	# plot heatmap
	m.add_child(plugins.HeatMap(stationArr, radius=15))
	
def plot_all(dataframed_data, color_code, color_set, m):
	for i in range(1,len(dataframed_data)):
		#change color upon change track_id
		if (dataframed_data.iloc[i-1]['track_id'] != dataframed_data.iloc[i]['track_id']):
			change_color(color_set)
			folium.Marker([dataframed_data.iloc[i]['latitude'], dataframed_data.iloc[i]['longitude']], popup = dataframed_data.iloc[i]['time'], icon = folium.Icon(color=color_set[color_code])).add_to(m) 
		else:
			folium.Marker([dataframed_data.iloc[i]['latitude'], dataframed_data.iloc[i]['longitude']], popup = dataframed_data.iloc[i]['time'], icon = folium.Icon(color=color_set[color_code])).add_to(m)
	
def save_map(save_name, m):
	#save map to current directory
	print("Map created, save to:", save_name)
	m.save(save_name)
	
def main():
	
	#Value area:
	# Set Default map location
	DEF_LAT = -10.93934139
	DEF_LON = -37.06274211

	select_flag = 'y'

	#Map name
	save_name = 'Map_Created.html'

	# read data from csv file (Ask for file location)
	print("Reading Data From File...")
	data_name = pd.read_csv("25_car.csv")
	print("Framing Data...")
	dataframed_data = pd.DataFrame(data_name)
	
	display_Data_Info(data_name)
	specify_map_attr()
	m = creat_map(DEF_LON,DEF_LAT)
	print("Basic Layer Creation successful!")
	
	#Data manipulation area
	ID_grouped = dataframed_data.groupby('track_id')
	
	All_flag = input("Plot All polints? (y/n): ")
	if All_flag == 'y':
		plot_all(dataframed_data, color_code, color_set, m)
		select_flag = 'n'
	
	while select_flag != 'n':
		select_group = eval(input("Please input the Track id number you wish to display: "))
		if select_group <= 25:
			temp_trackID = ID_grouped.get_group(select_group)
			#Extract lat and lon
			print("Extracting Lattitude and Longitude...")
			temp_long = list(temp_trackID.longitude)
			temp_lati = list(temp_trackID.latitude)
			temp_tuple = list(zip(temp_lati, temp_long))
			#For each track id, select below options
			marker_flag = input("Plot marker? (y/n): ")
			if marker_flag == 'y':
				plot_marker(temp_trackID, color_code, color_set, m)
			
			line_flag = input("Plot line? (y/n): ")
			if line_flag == 'y':
				plot_line(temp_tuple, color_code, color_set, m)
			
			heat_flag = input("Plot heatmap? (y/n): ")
			if heat_flag == 'y':
				heatmap(temp_trackID, m)
			
			select_flag = input("Select another id? (y/n): ")
			if select_flag == 'y':
				change_color(color_set)
				continue
			else:
				select_flag = 'n'
				break
		else:
			print("Please select another id.")
			continue
	
	save_map(save_name, m)

if __name__== "__main__":
	main()
	
	
'''	
#Plot all the points 	
for i in range(1,len(dataframed_data)):
		#change color upon change track_id
		if (dataframed_data.iloc[i-1]['track_id'] != dataframed_data.iloc[i]['track_id']):
			changeColor()
			folium.Marker([dataframed_data.iloc[i]['latitude'], dataframed_data.iloc[i]['longitude']], popup = dataframed_data.iloc[i]['time'], icon = folium.Icon(color=color_set[color_code])).add_to(m) 
		else:
			folium.Marker([dataframed_data.iloc[i]['latitude'], dataframed_data.iloc[i]['longitude']], popup = dataframed_data.iloc[i]['time'], icon = folium.Icon(color=color_set[color_code])).add_to(m)
	
'''

'''
	['red', 'blue', 'green', 'purple', 'orange', 'darkred',
		'lightred', 'beige', 'darkblue', 'darkgreen', 'cadetblue',
        'darkpurple', 'white', 'pink', 'lightblue', 'lightgreen',
        'gray', 'black', 'lightgray']

DEBUG LOG:

1. for loop will ignore very first data point, since it starts from 1.
'''
