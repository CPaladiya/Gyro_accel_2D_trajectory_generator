from math import cos,sin
import matplotlib.pyplot as plt
import matplotlib.animation as animation #This class would help me make the animation
import numpy as np

def velocity(accel_list,timestamp):
    
    """
    goal : creating list of velocity using list of acceleration and timestamps

    input : float type list of acceleration and timestamp

    output : float type list of veloctiy IMPORTANT : the length will be 1-length of accel_list

    """

    #checking if both timestamp and accel_list have the same length
    if len(accel_list) != len(timestamp):
        raise Exception("Acceleration and timestamp list length has to be same!")

    velocity = [] #defining an empty velocity list
    velo_at_i = 0 #defining velo_at_i for the loop
    for i in range(1,len(accel_list)):
        delta_time = timestamp[i]-timestamp[i-1] #calculating difference between consecutive timestamp
        velo_at_i += accel_list[i]*delta_time #calculating area under the graph for dt element
        velocity.append(velo_at_i) #adding that to the velocity list - area under the dt - velocity at dt

    return velocity

def yaw(gyro_list,timestamp):
    
    """
    goal : creating list of yaw using list of gyro_list(yaw rate data) and timestamps

    input : float type list of yawrate (gyro_list) and timestamp

    output : float type list of yaw  IMPORTANT : the length will be 1-length of gyro_list

    """

    #checking if both timestamp and gyro_list(yaw_rate) have the same length
    if len(gyro_list) != len(timestamp):
        raise Exception("Gyro and timestamp list length has to be same!")

    yaw = [] #defining an empty velocity list
    yaw_at_i = 0 #defining yaw_at_i for the loop
    for i in range(1,len(gyro_list)):
        delta_time = timestamp[i]-timestamp[i-1] #calculating difference between consecutive timestamp
        yaw_at_i += gyro_list[i]*delta_time #calculating area under the graph for dt element
        yaw.append(yaw_at_i) #adding that to the yaw list - area under the dt - yaw at dt

    return yaw

def get_x_y_list(velo,yaw,timestamp):

    """
    goal : creating list of x,y points using list of velocity and yaw

    input : float type list of velocity, yaw, timestamp (the sametime stamp used to create velo and yaw)

    output : float type list of (x,y) coordinates

    """
    x = 0
    y = 0
    x_y_list = [(x,y)]
    time = timestamp[1:]


    #print(len(velo))
    #print(len(yaw))
    #print(len(timestamp))

    #check if three lists have the same length
    if len(velo)!=len(yaw) or len(yaw)!=len(timestamp)-1 or len(timestamp)-1 != len(velo):
        raise Exception("yaw, velcoty list length has to be same and timestamp 1 len longer than the other two!")

    for i in range(1,len(time)):
        delta_t = time[i]-time[i-1]
        x += cos(yaw[i])*(velo[i]*delta_t)
        y += sin(yaw[i])*(velo[i]*delta_t)
        x_y_list.append((x,y))
    return x_y_list

def show_path(x_y_list):

    """
    goal : showing graph of x,y points in form of connected dots

    input : x_y points in terms of list [(x1,y1),(x2,y2),....]

    output : graph of connected x_y points in form of path

    """
    #creating x and y axis using x_y list
    X=[p[0] for p in x_y_list]
    Y=[p[1] for p in x_y_list]
    
    #setting up the main figure, axis, and plotting the elements we want to animate
    fig = plt.figure()
    ax = plt.subplot(111)
    ax.set(xlim=((min(X)-0.1),(max(X)+0.1)), ylim = ((min(Y)-0.1),(max(Y)+0.1)))
    plt.xlabel("Meters")
    plt.ylabel("Meters")
    plt.title("2D Trajectory Visualizer using Accelerometer and Gyro data.")
    
    sct = ax.scatter(x=X[0], y=Y[0])
    
    #animation function
    def animate(i):
        x = X[:i]
        y = Y[:i]
        sct.set_offsets(np.c_[x,y])
        return sct,
    
    #calling the animator blit = true - only draw the part of the graph that has changed
    
    anim = animation.FuncAnimation(fig,animate,frames = len(Y), interval = 2, blit = True)
    plt.show()