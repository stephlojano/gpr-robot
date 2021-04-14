from movement import *
def up_left_diag_filler_function(*args):
    shift_left(speed)
    print("GPR Robot is moving up left diagonal") 

def up_right_diag_filler_function(*args):
    shift_right(speed)
    print("GPR Robot is moving up right diagonal") 

def go_ahead_filler(speed, *args):
    go_ahead(speed)
    print("GPR Robot is moving forward")

def turn_left_filler(speed, *args):
    turn_left(speed)
    print("GPR Robot is turning left")

def turn_right_filler(speed, *args):
    turn_right(speed)
    print("GPR Robot is turning right")

def go_back_filler(speed, *args):
    go_back(speed)
    print("GPR Robot is going back")

def go_back_filler(*args):
    stop_car()
    print("GPR Robot stopped")

control_options = {
    "w": {
        "text":"Forward", 
        "function": go_ahead_filler
    },
    "a": {
        "text": "Left",
        "function": turn_left_filler
    },
    "s": {
        "text": "Back",
        "function": go_back_filler
    },
    "d" :{ 
        "text": "Right",
        "function": turn_right_filler
    },
    "q" : {
        "text": "Parallel left shift",
        "function": up_left_diag_filler_function
    },
    "e" : {
        "text": "Parallel Right Shift",
        "function": up_right_diag_filler_function
    },
    "f" : {
        "text": "Stop",
        "function": stop_movement_filler
    },
    # "c" : {
    #     "text": "Quit control panel",
    #     "function": filler_function
    # }
}
