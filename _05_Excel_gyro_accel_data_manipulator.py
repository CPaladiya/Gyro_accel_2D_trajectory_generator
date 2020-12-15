import xlrd as xl #to access the data from excel workbook
from Velo_yaw_from_accel_yawrate import velocity, yaw, get_x_y_list, show_path
#import xlswriter as xlw #to write the data in excel workbook

# ------------------------------ Loading the excel file ----------------------------------------------#
#name of the file to be accessed
path = 'Loop2.xlsx'

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
#print(worksheet.cell_value(1,0))

# ------------------------- collecting raw timestamp, accel and gyro data --------------------------------- #

timestamp_raw = [] #to collect first column as a time stamp list
accel_raw = [] #collect second column as a accel data list
gyro_raw = [] #collect third column as gyro data list
accel_adjust = 0.11
gyro_adjust = 0.008

for i in range(1,Y):
    #creating a list of timestamp using the raw data available in the first column
    timestamp_raw.append(float(worksheet.cell_value(i,0)))
    #creating a list of accel_meter data available in the second column
    #regardless of numeric data type of excel data, here it would be stored as float
    accel_raw.append(float(worksheet.cell_value(i,1)) + accel_adjust) #0.1 is an offset to mask the sensor error, adjust accordingly
    #creating a list of gyro data available in the third column
    #regardless of numeric data type of excel data, here it would be stored as float
    gyro_raw.append(float(worksheet.cell_value(i,2)) - gyro_adjust) #-0.004 is an offset to mask the sensor error, adjust accordingly
#print(len(timestamp_raw))
#print(len(accel_raw))
#print(len(gyro_raw))

# ------------------------- making a dict to collect data for unique timestamp --------------------------------- #

#there are multiple accel and gyro data for same timestamp, so creating dict to create data for unique timestamp
#example - {123456 : {'accel':[0.23,0.4,0.2], 'gyro':[0.45,0.2,0.4]}}

timestamp_dict = dict()
for i,time_stamp in enumerate(timestamp_raw):
    #to do - check if the entry is in the dict
    if time_stamp not in timestamp_dict:
        timestamp_dict[time_stamp] = {'accel':[accel_raw[i]], 'gyro':[gyro_raw[i]]}
    else:
        timestamp_dict[time_stamp]['accel'].append(accel_raw[i])
        timestamp_dict[time_stamp]['gyro'].append(gyro_raw[i])
#print('timestamp_dict : {}'.format(timestamp_dict))

# ------------------------ making useful list of unique timestamps and relevant accel, gyro data -----------------------#

timestamp = [] #unit seconds
accel = [] #unit meter per second squred
gyro = [] #rad per second

#condensing list of accel and gyro to a single avg of the list
for time_stamp,values in timestamp_dict.items():
    timestamp.append(time_stamp/1000) #converting timestamps into seconds with 1000
    accel.append(sum(timestamp_dict[time_stamp]['accel'])/len(timestamp_dict[time_stamp]['accel']))
    gyro.append(sum(timestamp_dict[time_stamp]['gyro'])/len(timestamp_dict[time_stamp]['gyro']))
#print('timestamp : {}'.format(timestamp))
#print('timestamp : {}'.format(timestamp))
#print('accel : {}'.format(accel))
#print('gyro : {}'.format(gyro))
#print(len(timestamp))
#print(len(accel))
#print(len(gyro))

# ------------------------ using timestamp and accel data to create 2D trajectory -----------------------#

true_velocity = velocity(accel,timestamp)
#print(len(true_velocity))
true_yaw = yaw(gyro,timestamp)
#print(len(true_yaw))
true_x_y_points = get_x_y_list(true_velocity,true_yaw, timestamp)
show_path(true_x_y_points)

