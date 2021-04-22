'''
 This file allows users to input dimensions of a feild to be scanned 
 The robot will use those dimensions to scan the area in a snake pattern
'''
from movement import *
import time
from math import pi

rpm = 225
wheel_diameter = 0.08 # in meters
robot_length = 0.3 # in meters
wheel_circumference = pi*wheel_diameter # in meters
single_rotation_speed = ((1/rpm) * 60) # This gives the time it takes for the wheel to make a single rotation in seconds
                                       # From my calculations each rotation covers approximately 0.2513 meters
                                       # So every "single_rotation_speed" the robot moves 0.2513 meters

robot_speed = wheel_circumference / single_rotation_speed # gives robot speed in meters per second -> approximately 0.9423 m/s
speed = 100 # Input for movement functions

'''
    METHOD FOR TRAVERSAL
        1. Robot moves forward full length in the y direction
        2. Robot rotates right 90 degrees
        3. Robot moves forward 0.3 meter (~length of robot) in the x direction
        4. Robot rotates right 90 degrees
        5. Robot moves forward in the -y direction
        6. Robot rotates left 90 degrees
        7. Robot moves forward 0.3 meter (~length of robot) in the x direction
        8. Robot rotates left 90 degrees
        9. If x length is not equal to full length then repeat until length in x is completed 

    '''

def forward_full_y(t_y):
    go_ahead(speed) 
    time.sleep(t_y)
    stop_car()
    time.sleep(1)

def rotate_right_90():
    turn_right(100) # STEP 2
    time.sleep(0.35) # Determined by testing rotation function for a  90 degree turn
    stop_car()
    time.sleep(1)

def forward_x(t_x):
    go_ahead(speed) # STEP 3
    time.sleep(t_x)
    stop_car()
    time.sleep(1)

def reverse_full_y(t_y):
    go_back(speed) # STEP 5
    time.sleep(t_y)
    stop_car()
    time.sleep(1)

def rotate_left_90():
    turn_left(100) # STEP 6
    time.sleep(0.35) # Determined by testing rotation function for a  90 degree turn
    stop_car()
    time.sleep(1)


def auto_move(x , y):

    # v = d / t   -----> t = d / v
    t_x = robot_length / robot_speed  # Time required to move 0.3 meters in x direction 
    t_y = y / robot_speed  # Time required to move length in y direction 

    print("Time x = " + str(t_x) + " Time y = " + str(t_y))

    x_counter = 0
    while(x_counter <= x):
        forward_full_y(t_y)
        rotate_right_90()
        forward_x(t_x)
        rotate_right_90()
        reverse_full_y(t_y)
        rotate_left_90()
        forward_x(t_x)
        rotate_left_90()

        x_counter += 0.3 # Increment the counter by the distance moved in x
        x_counter += 0.3 # Increment the counter by the distance moved in x

    #TODO: Might have to add one more forward_full_y outside loop before finishing
    stop_car()



auto_move(1.5,1.5) # 5ft x 5ft