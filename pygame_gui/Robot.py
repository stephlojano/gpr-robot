"""
This file creates a robot class which simplifies using the movement.py file
Instead of importing the file and using the functions, the goal is the instantiate a robot object
The robot object will then be used to call the movement functions

This file will also incorperate movement with the encoders so the robot can move based on inputted distance 
"""

import RPi.GPIO as GPIO  # control motor board through GPIO pins
from time import sleep

GPIO.setmode(GPIO.BCM)


class Robot:
    def __init__(self):
        self.IN1Rear = 12  # GPIO12 to IN1 Rear-right wheel direction
        self.IN2Rear = 16  # GPIO16 to IN2 Rear-right wheel direction

        # REAR LEFT MOTOR PINS
        self.IN3Rear = 20  # GPIO20 to IN3 Rear-left wheel direction
        self.IN4Rear = 21  # GPIO21 to IN4 Rear-left wheel direction

        # REAR ENA/ENB - duty cycle pins
        self.ENA_Rear = 26  # GPIO26 to ENA PWM SPEED of rear left motor
        self.ENB_Rear = 19  # GPIO19 to ENB PWM SPEED of rear right motor

        # FRONT LEFT MOTOR PINS
        self.IN1Front = 23  # GPIO23 to IN1 Front Model X left wheel direction
        self.IN2Front = 18  # GPIO18 to IN2 Front Model X left wheel direction

        # FRONT RIGHT MOTOR PINS
        self.IN3Front = 15  # GPIO15 to IN3 Front Model X right wheel direction
        self.IN4Front = 14  # GPIO14 to IN4 Front Model X right wheel direction

        # FRONT ENA/ENB - duty cycle pins
        self.ENA_Front = 25  # GPIO25 to ENA PWM SPEED of front left motor
        self.ENB_Front = 24  # GPIO24 to ENB PWM SPEED of front right motor

        # initialize Rear GPIO pins to be outputs
        GPIO.setup(self.IN1Rear, GPIO.OUT)
        GPIO.setup(self.IN2Rear, GPIO.OUT)
        GPIO.setup(self.IN3Rear, GPIO.OUT)
        GPIO.setup(self.IN4Rear, GPIO.OUT)
        GPIO.setup(self.ENA_Rear, GPIO.OUT)
        GPIO.setup(self.ENB_Rear, GPIO.OUT)

        # initialize Front GPIO pins to be outputs
        GPIO.setup(self.IN1Front, GPIO.OUT)
        GPIO.setup(self.IN2Front, GPIO.OUT)
        GPIO.setup(self.IN3Front, GPIO.OUT)
        GPIO.setup(self.IN4Front, GPIO.OUT)
        GPIO.setup(self.ENA_Front, GPIO.OUT)
        GPIO.setup(self.ENB_Front, GPIO.OUT)

        # initialize max frequency (aka speed)
        self.rrSpeed = GPIO.PWM(self.ENA_Rear, 100)
        self.rlSpeed = GPIO.PWM(self.ENB_Rear, 100)
        self.frSpeed = GPIO.PWM(self.ENA_Front, 100)
        self.flSpeed = GPIO.PWM(self.ENB_Front, 100)

        # set starting speed
        self.rrSpeed.start(0)
        self.rlSpeed.start(0)
        self.frSpeed.start(0)
        self.flSpeed.start(0)

    # The __init__ sets up all the input pins
    # The next functions use them to set up movement of the motors

    # Rear Right Motor Forward
    def rr_ahead(self):
        GPIO.output(self.IN1Rear, GPIO.LOW)
        GPIO.output(self.IN2Rear, GPIO.HIGH)

    # Rear Left Motor Forward
    def rl_ahead(self):
        # Rear left motor was wired opposite
        GPIO.output(self.IN3Rear, GPIO.LOW)
        GPIO.output(self.IN4Rear, GPIO.HIGH)

    # Rear Right Motor Reverse
    def rr_back(self):
        GPIO.output(self.IN1Rear, GPIO.HIGH)
        GPIO.output(self.IN2Rear, GPIO.LOW)

    # Rear Left Motor Reverse
    def rl_back(self):
        # Rear left motor was wired opposite
        GPIO.output(self.IN3Rear, GPIO.HIGH)
        GPIO.output(self.IN4Rear, GPIO.LOW)

    # Front Right Motor Forward
    def fl_ahead(self):
        GPIO.output(self.IN1Front, GPIO.HIGH)
        GPIO.output(self.IN2Front, GPIO.LOW)

    # Front Left Motor Forward
    def fr_ahead(self):
        GPIO.output(self.IN3Front, GPIO.LOW)
        GPIO.output(self.IN4Front, GPIO.HIGH)

    # Front Right Motor Reverse
    def fl_back(self):
        GPIO.output(self.IN1Front, GPIO.LOW)
        GPIO.output(self.IN2Front, GPIO.HIGH)

    # Front Left Motor Reverse
    def fr_back(self):
        GPIO.output(self.IN3Front, GPIO.HIGH)
        GPIO.output(self.IN4Front, GPIO.LOW)

    def change_duty_cycle(self, speed):
        if speed > 100 or speed < 0:
            print("Speed cannot be greater than 100 or less than 0")
        else:
            self.rrSpeed.ChangeDutyCycle(speed)
            self.rlSpeed.ChangeDutyCycle(speed)
            self.frSpeed.ChangeDutyCycle(speed)
            self.flSpeed.ChangeDutyCycle(speed)

    # Forward
    def go_ahead(self, speed=50):
        self.change_duty_cycle(speed)
        self.rl_ahead()
        self.rr_ahead()
        self.fl_ahead()
        self.fr_ahead()

    # Reverse
    def go_back(self, speed=50):
        self.change_duty_cycle(speed)
        self.rr_back()
        self.rl_back()
        self.fr_back()
        self.fl_back()

    # making right turn
    def turn_right(self, speed=50):
        self.change_duty_cycle(speed)
        self.rl_ahead()
        self.rr_back()
        self.fl_ahead()
        self.fr_back()

    # make left turn
    def turn_left(self, speed=50):
        self.change_duty_cycle(speed)
        self.rr_ahead()
        self.rl_back()
        self.fr_ahead()
        self.fl_back()

    # parallel left shift
    def shift_left(self, speed=50):
        self.change_duty_cycle(speed)
        self.fr_ahead()
        self.rr_back()
        self.rl_ahead()
        self.fl_back()

    # parallel right shift
    def shift_right(self, speed=50):
        self.change_duty_cycle(speed)
        self.fr_back()
        self.rr_ahead()
        self.rl_back()
        self.fl_ahead()

    # Diagonal Movement
    def upper_right(self, speed=50):
        self.change_duty_cycle(speed)
        self.rr_ahead()
        self.fl_ahead()

    def lower_left(self, speed=50):
        self.change_duty_cycle(speed)
        self.rr_back()
        self.fl_back()

    def upper_left(self, speed=50):
        self.change_duty_cycle(speed)
        self.fr_ahead()
        self.rl_ahead()

    def lower_right(self, speed=50):
        self.change_duty_cycle(speed)
        self.fr_back()
        self.rl_back()

    # make motors stop set all outputs to false
    def stop_car(self):
        self.change_duty_cycle(0)
