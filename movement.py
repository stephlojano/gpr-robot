import RPi.GPIO as GPIO #control motor board through GPIO pins
import time #set delay time to control moving distance


# IN1,2,3... are inputs on the motor driver that will connect to GPIO Pins
# Then by telling the pins to go high or low (GPIO.HIGH / GPIO.LOW) we can make 
#  the motor go forward or back

# REAR RIGHT MOTOR PINS
IN1Rear = 12 #GPIO12 to IN1 Rear-right wheel direction
IN2Rear = 16 #GPIO16 to IN2 Rear-right wheel direction

# REAR LEFT MOTOR PINS
IN3Rear = 20 #GPIO20 to IN3 Rear-left wheel direction
IN4Rear = 21 #GPIO21 to IN4 Rear-left wheel direction

# REAR ENA/ENB - duty cycle pins
ENA_Rear = 26 #GPIO26 to ENA PWM SPEED of rear left motor
ENB_Rear = 19 #GPIO19 to ENB PWM SPEED of rear right motor


# FRONT LEFT MOTOR PINS
IN1Front = 23 #GPIO23 to IN1 Front Model X left wheel direction
IN2Front = 18 #GPIO18 to IN2 Front Model X left wheel direction

# FRONT RIGHT MOTOR PINS
IN3Front = 15 #GPIO15 to IN3 Front Model X right wheel direction
IN4Front = 14 #GPIO14 to IN4 Front Model X right wheel direction

# FRONT ENA/ENB - duty cycle pins
ENA_Front = 25 #GPIO25 to ENA PWM SPEED of front left motor
ENB_Front = 24 #GPIO24 to ENB PWM SPEED of front right motor

#initialize Rear GPIO pins to be outputs
GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1Rear, GPIO.OUT) 
GPIO.setup(IN2Rear, GPIO.OUT)
GPIO.setup(IN3Rear, GPIO.OUT)
GPIO.setup(IN4Rear, GPIO.OUT)
GPIO.setup(ENA_Rear, GPIO.OUT)
GPIO.setup(ENB_Rear, GPIO.OUT)

#initialize Front GPIO pins to be outputs
GPIO.setup(IN1Front, GPIO.OUT) 
GPIO.setup(IN2Front, GPIO.OUT)
GPIO.setup(IN3Front, GPIO.OUT)
GPIO.setup(IN4Front, GPIO.OUT)
GPIO.setup(ENA_Front, GPIO.OUT)
GPIO.setup(ENB_Front, GPIO.OUT)


#GPIO.output(ENA,True)
#GPIO.output(ENB,True)

# Rotation Speed (base set to 100 Anything lower cause squealing)
rrSpeed = GPIO.PWM(ENA_Rear,1000)
rlSpeed = GPIO.PWM(ENB_Rear,1000)
frSpeed = GPIO.PWM(ENA_Front,1000)
flSpeed = GPIO.PWM(ENB_Front,1000)

rrSpeed.start(100)
rlSpeed.start(100)
frSpeed.start(100)
flSpeed.start(100)


# Function to change rotation speed
def change_duty_cycle(speed):
    rrSpeed.ChangeDutyCycle(speed)
    rlSpeed.ChangeDutyCycle(speed)
    frSpeed.ChangeDutyCycle(speed)
    flSpeed.ChangeDutyCycle(speed)


# Rear Right Motor Forward
# Can use speed input for change duty cycle
def rr_ahead(speed):
    GPIO.output(IN1Rear,GPIO.LOW)
    GPIO.output(IN2Rear,GPIO.HIGH)


# Rear Left Motor Forward
def rl_ahead(speed):
    GPIO.output(IN3Rear,GPIO.LOW)
    GPIO.output(IN4Rear,GPIO.HIGH)
    
    
# Rear Right Motor Reverse
def rr_back(speed):
    GPIO.output(IN1Rear,GPIO.HIGH)
    GPIO.output(IN2Rear,GPIO.LOW)


# Rear Left Motor Reverse
def rl_back(speed):  
    GPIO.output(IN3Rear,GPIO.HIGH)
    GPIO.output(IN4Rear,GPIO.LOW)
    
    
# Front Right Motor Forward
def fl_ahead(speed):
    GPIO.output(IN1Front,GPIO.LOW)
    GPIO.output(IN2Front,GPIO.HIGH)


# Front Left Motor Forward
def fr_ahead(speed):  
    GPIO.output(IN3Front,GPIO.LOW)
    GPIO.output(IN4Front,GPIO.HIGH)
 
    
# Front Right Motor Reverse
def fl_back(speed):
    GPIO.output(IN1Front,GPIO.LOW)
    GPIO.output(IN2Front,GPIO.HIGH)

# Front Left Motor Reverse
def fr_back(speed):  
    GPIO.output(IN3Front,GPIO.HIGH)
    GPIO.output(IN4Front,GPIO.LOW)

    
# Forward
def go_ahead(speed):
    rl_ahead(speed)
    rr_ahead(speed)
    fl_ahead(speed)
    fr_ahead(speed)
   
# Reverse
def go_back(speed):
    rr_back(speed)
    rl_back(speed)
    fr_back(speed)
    fl_back(speed)

#making right turn   
def turn_right(speed):
    rl_ahead(speed)
    rr_back(speed)
    fl_ahead(speed)
    fr_back(speed)
      
#make left turn
def turn_left(speed):
    rr_ahead(speed)
    rl_back(speed)
    fr_ahead(speed)
    fl_back(speed)

# parallel left shift 
def shift_left(speed):
    fr_ahead(speed)
    rr_back(speed)
    rl_ahead(speed)
    fl_back(speed)

# parallel right shift 
def shift_right(speed):
    fr_back(speed)
    rr_ahead(speed)
    rl_back(speed)
    fl_ahead(speed)


# Diagonal Movement
def upper_right(speed):
    rr_ahead(speed)
    fl_ahead(speed)

def lower_left(speed):
    rr_back(speed)
    fl_back(speed)
    
def upper_left(speed):
    fr_ahead(speed)
    rl_ahead(speed)

def lower_right(speed):
    fr_back(speed)
    rl_back(speed)

#make motors stop set all outputs to false 
def stop_car():
    GPIO.output(IN1Rear,GPIO.LOW)
    GPIO.output(IN2Rear,GPIO.LOW)
    GPIO.output(IN3Rear,GPIO.LOW)
    GPIO.output(IN4Rear,GPIO.LOW)
    GPIO.output(IN1Front,GPIO.LOW)
    GPIO.output(IN2Front,GPIO.LOW)
    GPIO.output(IN3Front,GPIO.LOW)
    GPIO.output(IN4Front,GPIO.LOW)
    #rrSpeed.ChangeDutyCycle(0)
    #rlSpeed.ChangeDutyCycle(0)
    #frSpeed.ChangeDutyCycle(0)
    #flSpeed.ChangeDutyCycle(0)
    



    
