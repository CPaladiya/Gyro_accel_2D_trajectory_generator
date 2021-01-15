import xlrd as xl #to access the data from excel workbook
from Velo_yaw_from_accel_yawrate import velocity, yaw, get_x_y_list, show_path
#import xlswriter as xlw #to write the data in excel workbook

# ------------------------------ Loading the excel file ----------------------------------------------#
#name of the file to be accessed
path = 'Pulse.xlsx'

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

timestamp = [] #to collect first column as a time stamp list
accel = [] #collect second column as a accel data list
gyro = [] #collect third column as gyro data list
# step1 : straighten the graph by adjusting gyro_adjust, then adjust accel_adjust
accel_adjust = 0 # offset to mask the sensor error, please adjust accordingly
gyro_adjust = 0 # offset to mask the sensor error, please adjust accordingly

for i in range(1,Y):
    #creating a list of timestamp using the raw data available in the first column
    timestamp.append(float((worksheet.cell_value(i,0))/1000))
    #creating a list of accel_meter data available in the second column
    #regardless of numeric data type of excel data, here it would be stored as float
    accel.append(float(worksheet.cell_value(i,1)) + accel_adjust)
    #creating a list of gyro data available in the third column
    #regardless of numeric data type of excel data, here it would be stored as float
    gyro.append(float(worksheet.cell_value(i,2)) + gyro_adjust) 
#print(len(timestamp_raw))
#print(len(accel_raw))
#print(len(gyro_raw))

# ------------------------ using timestamp and accel data to create 2D trajectory -----------------------#

true_velocity = velocity(accel,timestamp)
#print(len(true_velocity))
true_yaw = yaw(gyro,timestamp)
#print(len(true_yaw))
true_x_y_points = get_x_y_list(true_velocity,true_yaw, timestamp)
show_path(true_x_y_points)

