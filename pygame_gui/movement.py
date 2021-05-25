import RPi.GPIO as GPIO  # control motor board through GPIO pins
import time  # set delay time to control moving distance


# IN1,2,3... are inputs on the motor driver that will connect to GPIO Pins
# Then by telling the pins to go high or low (GPIO.HIGH / GPIO.LOW) we can make
#  the motor go forward or back

# REAR RIGHT MOTOR PINS
IN1Rear = 12  # GPIO12 to IN1 Rear-right wheel direction
IN2Rear = 16  # GPIO16 to IN2 Rear-right wheel direction

# REAR LEFT MOTOR PINS
IN3Rear = 20  # GPIO20 to IN3 Rear-left wheel direction
IN4Rear = 21  # GPIO21 to IN4 Rear-left wheel direction

# REAR ENA/ENB - duty cycle pins
ENA_Rear = 26  # GPIO26 to ENA PWM SPEED of rear left motor
ENB_Rear = 19  # GPIO19 to ENB PWM SPEED of rear right motor

# FRONT LEFT MOTOR PINS
IN1Front = 23  # GPIO23 to IN1 Front Model X left wheel direction
IN2Front = 18  # GPIO18 to IN2 Front Model X left wheel direction

# FRONT RIGHT MOTOR PINS
IN3Front = 15  # GPIO15 to IN3 Front Model X right wheel direction
IN4Front = 14  # GPIO14 to IN4 Front Model X right wheel direction

# FRONT ENA/ENB - duty cycle pins
ENA_Front = 25  # GPIO25 to ENA PWM SPEED of front left motor
ENB_Front = 24  # GPIO24 to ENB PWM SPEED of front right motor

# initialize Rear GPIO pins to be outputs
GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1Rear, GPIO.OUT)
GPIO.setup(IN2Rear, GPIO.OUT)
GPIO.setup(IN3Rear, GPIO.OUT)
GPIO.setup(IN4Rear, GPIO.OUT)
GPIO.setup(ENA_Rear, GPIO.OUT)
GPIO.setup(ENB_Rear, GPIO.OUT)

# initialize Front GPIO pins to be outputs
GPIO.setup(IN1Front, GPIO.OUT)
GPIO.setup(IN2Front, GPIO.OUT)
GPIO.setup(IN3Front, GPIO.OUT)
GPIO.setup(IN4Front, GPIO.OUT)
GPIO.setup(ENA_Front, GPIO.OUT)
GPIO.setup(ENB_Front, GPIO.OUT)

# Rotation Speed (base set to 100 anything less causes squealing)
rrSpeed = GPIO.PWM(ENA_Rear, 1000)
rlSpeed = GPIO.PWM(ENB_Rear, 1000)
frSpeed = GPIO.PWM(ENA_Front, 1000)
flSpeed = GPIO.PWM(ENB_Front, 1000)

rrSpeed.start(100)
rlSpeed.start(100)
frSpeed.start(100)
flSpeed.start(100)


# Function to change rotation speed
def change_duty_cycle(speed):
    if speed < 100:
        print("Speed cannot be less than 100")
    else:
        rrSpeed.ChangeDutyCycle(speed)
        rlSpeed.ChangeDutyCycle(speed)
        frSpeed.ChangeDutyCycle(speed)
        flSpeed.ChangeDutyCycle(speed)


# Rear Right Motor Forward
def rr_ahead():
    GPIO.output(IN1Rear, GPIO.LOW)
    GPIO.output(IN2Rear, GPIO.HIGH)


# Rear Left Motor Forward
def rl_ahead():
    # Rear left motor was wired opposite
    GPIO.output(IN3Rear, GPIO.LOW)
    GPIO.output(IN4Rear, GPIO.HIGH)


# Rear Right Motor Reverse
def rr_back():
    GPIO.output(IN1Rear, GPIO.HIGH)
    GPIO.output(IN2Rear, GPIO.LOW)


# Rear Left Motor Reverse
def rl_back():
    # Rear left motor was wired opposite
    GPIO.output(IN3Rear, GPIO.HIGH)
    GPIO.output(IN4Rear, GPIO.LOW)


# Front Right Motor Forward
def fl_ahead():
    GPIO.output(IN1Front, GPIO.HIGH)
    GPIO.output(IN2Front, GPIO.LOW)


# Front Left Motor Forward
def fr_ahead():
    GPIO.output(IN3Front, GPIO.LOW)
    GPIO.output(IN4Front, GPIO.HIGH)


# Front Right Motor Reverse
def fl_back():
    GPIO.output(IN1Front, GPIO.LOW)
    GPIO.output(IN2Front, GPIO.HIGH)


# Front Left Motor Reverse
def fr_back():
    GPIO.output(IN3Front, GPIO.HIGH)
    GPIO.output(IN4Front, GPIO.LOW)


# Forward
def go_ahead():
    rl_ahead()
    rr_ahead()
    fl_ahead()
    fr_ahead()


# Reverse
def go_back():
    rr_back()
    rl_back()
    fr_back()
    fl_back()


# making right turn
def turn_right():
    rl_ahead()
    rr_back()
    fl_ahead()
    fr_back()


# make left turn
def turn_left():
    rr_ahead()
    rl_back()
    fr_ahead()
    fl_back()


# parallel left shift
def shift_left():
    fr_ahead()
    rr_back()
    rl_ahead()
    fl_back()


# parallel right shift
def shift_right():
    fr_back()
    rr_ahead()
    rl_back()
    fl_ahead()


# Diagonal Movement
def upper_right():
    rr_ahead()
    fl_ahead()


def lower_left():
    rr_back()
    fl_back()


def upper_left():
    fr_ahead()
    rl_ahead()


def lower_right():
    fr_back()
    rl_back()


# make motors stop set all outputs to false
def stop_car():
    GPIO.output(IN1Rear, GPIO.LOW)
    GPIO.output(IN2Rear, GPIO.LOW)
    GPIO.output(IN3Rear, GPIO.LOW)
    GPIO.output(IN4Rear, GPIO.LOW)
    GPIO.output(IN1Front, GPIO.LOW)
    GPIO.output(IN2Front, GPIO.LOW)
    GPIO.output(IN3Front, GPIO.LOW)
    GPIO.output(IN4Front, GPIO.LOW)
