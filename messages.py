# from movement import *
def up_left_diag_filler_function(*args):
    print("GPR Robot is moving up left diagonal") 

def up_right_diag_filler_function(*args):
    print("GPR Robot is moving up right diagonal") 

def go_ahead_filler(*args):
    print("GPR Robot is moving forward")

def turn_left_filler(*args):
    print("GPR Robot is turning left")

def turn_right_filler(*args):
    print("GPR Robot is turning right")

def go_back_filler(*args):
    print("GPR Robot is going back")

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
        "text": "Rotate Counterclockwise",
        "function": up_left_diag_filler_function
    },
    "e" : {
        "text": "Rotate Clockwise",
        "function": up_right_diag_filler_function
    },
    # "c" : {
    #     "text": "Quit control panel",
    #     "function": filler_function
    # }
}
