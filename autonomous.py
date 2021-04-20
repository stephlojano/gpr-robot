# This file allows users to input dimensions of a feild to be scanned 
# The robot will use those dimensions to scan the area in a snake pattern

#from movement import *
import time
from math import pi

rpm = 225
wheel_diameter = 0.08 # in meters
wheel_circumference = pi*wheel_diameter # in meters

single_rotation_speed = ((1/rpm) * 60) # This gives the time it takes for the wheel to make a single rotation in seconds

# From my calculations each rotation covers approximately 0.2513 meters
# So every "single_rotation_speed" the robot moves 0.2513 meters

robot_speed = wheel_circumference / single_rotation_speed # gives robot speed in meters per second -> approximately 0.9423 m/s

def auto_move(x , y):
    # x is the width of the feild in meters
    # y is the length of the feild in meters

    # v = d / t   -----> t = d / v

    t_x = x / robot_speed # Time required to move width of the field
    t_y = y / robot_speed  # Time required to move length of the field

    print("Time x = " + str(t_x) + "   Time y = " + str(t_y))

    #go_ahead()
    time.sleep(t_y)

    #shift_right()
    time.sleep(t_x)
    
    #stop_car()

    #TODO: Make sure to also provide options for measurements in feet 
    #TODO: The time for left shifts could be different so change that later 




auto_move(2,2)
