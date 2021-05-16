'''
This file is for testing the encoder of the motors that we have

We will let the robot run and track the total number of states that 
    it goes through and use that to show the distance traveled
'''

from Robot import Robot
import RPi.GPIO as GPIO 

encoder = 17 # Set encoder pin

GPIO.setmode(GPIO.BCM)
GPIO.setup(encoder, GPIO.IN, pull_up_down = GPIO.PUD_UP) # Set the pin as input that recieves quick changes

state_last = GPIO.input(encoder)
rotation_count = 0
state_count = 0
state_count_total = 0

wheel_size = 247 # in mm
states_per_rotation = 312 # ratio = 30 reducer = 22 * 6
distance_per_state = wheel_size / states_per_rotation

robot = Robot()
robot.go_ahead()

try:
    while 1:
        state_current = GPIO.input(encoder)
        if state_current != state_last:
            state_last = state_current
            state_count += 1
            state_count_total += 1
        
        if state_count == states_per_rotation:
            rotation_count += 1
            state_count = 0

except KeyboardInterrupt: #CTRL: + C
    robot.stop_car()
    GPIO.cleanup()

distance = (distance_per_state * state_count_total) * 0.001 # in meters
print('Total distance traveled = ' + str(distance) + ' meters')
print('Total number of rotations = ' + str(rotation_count))
print('Total number of states = ' + str(state_count_total))