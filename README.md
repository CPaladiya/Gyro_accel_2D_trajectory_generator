# 05_Gyro_accel_2D_trajectory_generator
Program to generate 2D path trajectory using Accelerometer and Gyroscope data.

## Prerequisites
- Install [xlrd](https://pypi.org/project/xlrd/) python library
- Set path to your desired excel file on [Line-7](https://github.com/CPaladiya/05_Gyro_accel_2D_trajectory_generator/blob/de149134f0a75f889b87a045ae6b956c389257aa/_05_Excel_gyro_accel_data_manipulator.py#L7) within `_05_Excel_gyro_accel_data_manipulator.py`
- Make sure to save Excel file as `.xls` file (Save As Excel 97-2003 Workbook)
- Units for Timestamp - *milliseconds*, Linear accel. - *m/s<sup>2*, Gyroscopic accel. (Anglular accel.) - *rad/s<sup>2*

## Example of xls file
- Code collects data starting from the cell `A2`, `B2` and `C2`

![xls_details](https://user-images.githubusercontent.com/74514429/104867531-119fd100-590f-11eb-8eaf-4bd419284b7a.png)

### Calibration
- Modify offset `(Default offset = 0)` to accomodate sensor error or calibrate acceleration data on [Line 30/Line 31](https://github.com/CPaladiya/05_Gyro_accel_2D_trajectory_generator/blob/de149134f0a75f889b87a045ae6b956c389257aa/_05_Excel_gyro_accel_data_manipulator.py#L30-L31) within `_05_Excel_gyro_accel_data_manipulator.py`

## If you are using - 6 DOF+ IMU Sensor/Accelerometer
- Only two component is required for plotting 2D trajectory
- Correlate your usage of sensor with the image below
- Choose two appropreate components, one linear and one angular accel. component

![details](https://user-images.githubusercontent.com/74514429/104868378-2e3d0880-5911-11eb-9e35-123900ffe457.png)

