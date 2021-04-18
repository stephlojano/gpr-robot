# import Rpi.GPIO as GPIO
# from movement import *
import time
import tkinter as tk
from tkinter import messagebox # this is required by tkinter
from messages import *
import tkinter.ttk as ttk

# TODO: refactor after 03/02/2021 presentation 
# The goal to transform the main page (GUI window 1) into a class 
# and the controls page (GUI window 2) into a class in a SEPARATE file 
# then finally import both classes to a main file 

# controlling GPIO on RaspPi 

# GPIO.setmode(GPIO.BCM) # referring to pins by # after "GPIO"
# GPIO.setmode(GPIO.BOARD) # referring to pins by # of pin

# forward motion - w 

# left motion - a

# backward motion - s 

# right motion - d


root = tk.Tk()
root.title('Ground Penetrating Radar (GPR) Robot')

# creating a label widget
welcome_message = tk.Label(root, text='Welcome! \n Please enter the dimensions of the area to be covered.')

user_entry_dimension_x = tk.Entry(root, width=20, borderwidth=1)
user_entry_dimension_x.insert(tk.END, 'grid x dim')
user_entry_dimension_x.grid(row=4, column=1)

user_entry_dimension_y = tk.Entry(root, width=20, borderwidth=1)
user_entry_dimension_y.insert(tk.END, 'grid y dim')
user_entry_dimension_y.grid(row=5, column=1)


def second_window(x, y):
    x, y = float(x), float(y)
    control_panel = tk.Tk()
    control_panel.title('GPR Manual Cuntrol')

    grid_size_message = tk.Label(control_panel, text=f'Area: {x}m x {y}m\nTotal Area: {x*y} m^2')
    grid_size_message.grid(row=0, column=1)

    instructions_msg = tk.Label(control_panel, text="Instruction for Manual Control")
    instructions_msg.grid(row=1, column=1)

    ttk.Separator(control_panel, orient=tk.HORIZONTAL).grid(column=1, row=2, rowspan=1, sticky='ns')
    row = 3
    num_control_options = len(control_options)
    ttk.Separator(control_panel, orient=tk.VERTICAL).grid(column=1, row=row, rowspan=num_control_options, sticky='ns')
    for key, control in control_options.items():
        if key != 'c':
            control_option = tk.Button(control_panel, text=key, command=control["function"])
        else:
            control_option = tk.Button(control_panel, text=key, command=control_panel.quit)
        control_option.grid(row=row, column=0, padx=50)
        control_option = tk.Label(control_panel, text=control["text"])
        control_option.grid(row=row, column=2)
        row += 1

    row+=1
    control_option = tk.Button(control_panel, text="Exit Manual Control", command=control_panel.quit)
    control_option.grid(row=row, column=1, padx=50)

    # print(f"binding <{key}>")
    control_option.bind(f"<w>", control_options["w"]["function"])
    control_option.focus_set()
    control_option.bind(f"<a>", control_options["a"]["function"])
    control_option.focus_set()
    control_option.bind(f"<s>", control_options["s"]["function"])
    control_option.focus_set()
    control_option.bind(f"<d>", control_options["d"]["function"])
    control_option.focus_set()
    control_option.bind(f"<q>", control_options["q"]["function"])
    control_option.focus_set()
    control_option.bind(f"<e>", control_options["e"]["function"])
    control_option.focus_set()
    control_option.bind(f"<f>", control_options["f"]["function"])
    control_option.focus_set()
    





def clickOK():
    x_value_accepted, y_value_accepted = False, False
    entered_x_value, entered_y_value = user_entry_dimension_x.get(), user_entry_dimension_y.get()

    if entered_x_value.isnumeric() == tk.FALSE or entered_y_value.isnumeric() == tk.FALSE:
        try:
            entered_x_value = float(entered_x_value)
            x_value_accepted = True 
        except:
            messagebox.showwarning("Invalid x dimension", "Please enter numerical dimensions for x.")
        try:
            entered_y_value = float(entered_y_value)
            y_value_accepted = True 
        except:
            messagebox.showwarning("Invalid y dimension", "Please enter numerical dimensions for y.")
    else:
        x_value_accepted, y_value_accepted = True, True 

    if not all([x_value_accepted, y_value_accepted]):
        textClick = "Invalid value entered"
    else:
        textClick = "Initiating grid:\n({}m x {}m)".format(entered_x_value, entered_y_value) 
        second_window(entered_x_value, entered_y_value)

    enterDimen = tk.Label(root, text=textClick)
    enterDimen.grid(row=6, column=1)


def clear_button():
    user_entry_dimension_x.delete(0, tk.END)
    user_entry_dimension_y.delete(0, tk.END)


button_clear = tk.Button(root, text='Clear', command=clear_button)
buttonOK = tk.Button(root, text='OK', command=clickOK)

# TODO: fix this - enter not working 
# binding ENTER key to have same func as buttonOK
# buttonOK.bind('<Return>', lambda event: user_entry_dimension_x.get())
buttonOK.bind('<Return>', clickOK)


# render buttons and user entry box onto the GUI
welcome_message.grid(row=0, column=1)
buttonOK.grid(row=7, column=1)
button_clear.grid(row=8, column=1)

button_quit = tk.Button(root, text="Exit", command=root.quit)
button_quit.grid(row=9, column=1)

root.mainloop()









