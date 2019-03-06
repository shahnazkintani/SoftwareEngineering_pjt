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

# print (dataframed)

grouped = dataframed.groupby('track_id')
tid1 = grouped.get_group(1)
tid2 = grouped.get_group(2)
tid3 = grouped.get_group(3)
tid4 = grouped.get_group(4)

# print (tid1)

# extracting the latitiude and longitude column 
col_lat1 = list(tid1.latitude)

col_long1 = list(tid1.longitude)

col_lat2 = list(tid2.latitude)
col_long2 = list(tid2.longitude)

col_lat3 = list(tid3.latitude)
col_long3 = list(tid3.longitude)

col_lat4 = list(tid4.latitude)
col_long4 = list(tid4.longitude)

print (col_lat1)

#  append the first value in the last ot comple a loop
col_lat1.append(col_lat1[0])
col_long1.append(col_long1[0])
col_lat2.append(col_lat2[0])
col_long2.append(col_long2[0])
col_lat3.append(col_lat3[0])
col_long3.append(col_long3[0])
col_lat4.append(col_lat4[0])
col_long4.append(col_long4[0])
print (col_lat1)



# for g in grouped:
   
#     print (g)

