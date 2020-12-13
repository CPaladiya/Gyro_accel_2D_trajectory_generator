import xlrd as xl #to access the data from excel workbook
#import xlswriter as xlw #to write the data in excel workbook

#name of the file to be accessed
path = 'work_to_home_raw_data.xlsx'

#accessing the workbook itself
inputworkbook = xl.open_workbook(path)
#accessing the worksheet within that workbook, 0 is the index meaning first in the line
worksheet = inputworkbook.sheet_by_index(0)

#let's first see howmany rows and colums are there. 
#print(worksheet.ncols)
#print(worksheet.nrows)

Y=worksheet.nrows #number of rows from 1,2 to... in Excel file
X=worksheet.ncols  #number of cols from A,B, to .. in Excel file

#to access the cell value use worksheet.cell_value(Y,X) ex. (1,0) will give access to A2 cell
print(worksheet.cell_value(1,0))

timestamp_raw = [] #to collect first column as a time stamp list
#convert this timestamp_raw in to seconds
accel_raw = [] #collect second column as a accel data list
gyro_raw = [] #collect third column as gyro data list

for i in range(1,Y):
    #creating a list of timestamp using the raw data available in the first column
    timestamp_raw.append(worksheet.cell_value(i,0))
    #creating a list of accel_meter data available in the second column
    #regardless of numeric data type of excel data, here it would be stored as float
    accel_raw.append(worksheet.cell_value(i,1)) 
    #creating a list of gyro data available in the third column
    #regardless of numeric data type of excel data, here it would be stored as float
    gyro_raw.append(worksheet.cell_value(i,2)) 
#print(len(timestamp_raw))
#print(len(accel_raw))
#print(len(gyro_raw))

#creating timestamp dictionary to collect all the gyro and accel data for that time stamp
timestamp_dict = dict()
for time_stamp in timestamp_raw:
    #to do - check if the entry is in the dict
    if time_stamp not in timestamp_dict:
        timestamp_dict[time_stamp] = {'accel':[accel_raw[i]], 'gyro':[gyro_raw[i]]}
    else:
        timestamp_dict[time_stamp]['accel'].append(accel_raw[i])
        timestamp_dict[time_stamp]['gyro'].append(gyro_raw[i])

print(timestamp_dict)

#condensing list of accel and gyro to a single avg of the list

for time_stamp in timestamp_raw:
    timestamp_dict[time_stamp]['accel'] = sum[timestamp_dict[time_stamp]['accel']]/len(timestamp_dict[time_stamp]['accel'])
    timestamp_dict[time_stamp]['gyro'] = sum[timestamp_dict[time_stamp]['gyro']]/len(timestamp_dict[time_stamp]['gyro'])

    #write a program to add reduced time stamp, accel data and gyro data to the new workbook
    # to create the graph and visualize the data to make sense of changes
    # use this data to track the trajectory and try to further reduce it if its at all possible.