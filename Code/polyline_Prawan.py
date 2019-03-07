import folium
import pandas as pd 
import csv 

# read data from csv file
data = pd.read_csv("40_dp_test.csv")
# print (data.columns)
print (data.dtypes)

# print (data)

dataframed = pd.DataFrame(data)
print('dataframe success')

# #  To check the values in the csv file.
# with open('40_dp_test.csv', 'r') as csvFile:
#     reader = csv.reader(csvFile)
#     for row in reader:
#         print(row)

# csvFile.close()

# create map object
m = folium.Map(location =[-10.93934139,-37.06274211], zoom_start=12)

# print (dataframed)

grouped = dataframed.groupby('track_id')
tid1 = grouped.get_group(1)
tid2 = grouped.get_group(2)
tid3 = grouped.get_group(3)
tid4 = grouped.get_group(4)
# print (tid1)

# polyline l1
l1 = tid1.loc[:,'latitude':'longitude']
# print (l1)
p1 = l1.values.tolist()
# print (p1)
folium.PolyLine(locations=p1, color='blue').add_to(m)


# polyline l2
l2 = tid2.loc[:,'latitude':'longitude']
# print (l1)
p2 = l2.values.tolist()
# print (p1)
folium.PolyLine(locations=p2, color='green').add_to(m)

# polyline l3
l3 = tid3.loc[:,'latitude':'longitude']
# print (l1)
p3 = l3.values.tolist()
# print (p1)
folium.PolyLine(locations=p3, color='red').add_to(m)

# polyline l4
l4 = tid4.loc[:,'latitude':'longitude']
# print (l1)
p4 = l4.values.tolist()
# print (p1)
folium.PolyLine(locations=p4, color='purple').add_to(m)


# Generate map
m.save('polyline_Prawan.html')