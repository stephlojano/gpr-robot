'''
This file is for autonomous movement but the method is different from autonomous.py

In the autonomous.py file, a user would input how far the robot should move, and the function would then use that distance,
    to calcuate the time required to move that much distance. The movement function would then run for the calculated time

Although that works it would be much better to be able to tell the robot to move a certain amount forward directly. This can be done using 
the hall encoder that is built into the motor
'''

from Robot import Robot
from time import sleep
import RPi.GPIO as GPIO 

encoder = 17 # Set encoder pin

GPIO.setmode(GPIO.BCM)
GPIO.setup(encoder, GPIO.IN, pull_up_down = GPIO.PUD_UP) # Set the pin as input that recieves quick changes


wheel_size = 247 # in mm
states_per_rotation = 312 # ratio = 30 reducer = 22
distance_per_state = wheel_size / states_per_rotation # in mm

robot = Robot()
robot.change_duty_cycle(20)


# I wannna move 5 meters
# 5 meters / distance_per_state = 6250

def find_states(distance):
    distance_mm = distance * 1000 # Y will be in meters so we convert to milimeters
    total_states = distance_mm / distance_per_state 
    return total_states


def forward_full_y(total_states):
    state_last = GPIO.input(encoder)

    state_count_total = 0

    robot.go_ahead()

    while state_count_total <= total_states:
        state_current = GPIO.input(encoder)
        if state_current != state_last:
            state_last = state_current
            state_count_total += 1

    robot.stop_car()
    sleep(2)


def forward_x(total_states):
    state_last = GPIO.input(encoder)

    state_count_total = 0
    robot.go_ahead()

    while state_count_total <= total_states:
        state_current = GPIO.input(encoder)
        if state_current != state_last:
            state_last = state_current
            state_count_total += 1

    robot.stop_car()
    sleep(2)

def rotate_right():
    state_last = GPIO.input(encoder)

    state_count_total = 0
    robot.turn_right()

    while state_count_total <= 280:           # 257 found by calculation then experimenting
        state_current = GPIO.input(encoder)
        if state_current != state_last:
            state_last = state_current
            state_count_total += 1

    robot.stop_car()
    sleep(2)


def rotate_left():
    state_last = GPIO.input(encoder)

    state_count_total = 0
    robot.turn_left()

    while state_count_total <= 280:           # 257 found by calculation then experimenting
        state_current = GPIO.input(encoder)
        if state_current != state_last:
            state_last = state_current
            state_count_total += 1

    robot.stop_car()
    sleep(2)


def auto_move(x,y):
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

    y_total_states = find_states(y)
    x_total_states = find_states(0.25)

    x_counter = 0

    while(x_counter < x):
        forward_full_y(y_total_states)
        rotate_right()
        forward_x(x_total_states)
        rotate_right()
        forward_full_y(y_total_states)
        rotate_left()
        forward_x(x_total_states)
        rotate_left()

        x_counter += 0.50 # Increment the counter by the distance moved in x

    robot.stop_car()


auto_move(1,1)









