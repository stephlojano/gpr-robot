# import Rpi.GPIO as GPIO
import time
from tkinter import *
from tkinter import messagebox

# controlling GPIO on RaspPi 

# GPIO.setmode(GPIO.BCM) # referring to pins by # after "GPIO"
# GPIO.setmode(GPIO.BOARD) # referring to pins by # of pin

# forward motion - w 

# left motion - a

# backward motion - s 

# right motion - d




root = Tk()
root.title('Ground Penetrating Radar (GPR) Robot')

# creating a label widget
welcomeMsg = Label(root, text='Welcome! \n Please enter the dimensions of the area to be covered.')

e = Entry(root, width=40, borderwidth=5)
e.grid(row=4, column=5)



def clickOK():
    if e.get().isnumeric() == FALSE:
        messagebox.showwarning("Invalid dimensions", "Please enter numerical dimensions.")

    textClick = "You entered:\n" + e.get()
    enterDimen = Label(root, text=textClick)
    enterDimen.grid(row=5, column=5)

def clearButton():
    e.delete(0, END)

# def popup():
#     messagebox.showwarning("Invalid dimensions")



buttonClear = Button(root, text='Clear', command=clearButton)


buttonOK = Button(root, text='OK', command=clickOK)

# binding ENTER key to have same func as buttonOK
buttonOK.bind('<Return>', lambda event: e.get())
# myButton2 = Button(root, text='Cancel')

# onto the screen 
welcomeMsg.grid(row=0, column=5)
buttonOK.grid(row=6, column=5)
# myButton2.grid(row=1, column=2)
buttonClear.grid(row=4, column=6)

buttonQuit = Button(root, text="Exit", command=root.quit)
buttonQuit.grid(row=7, column=5)

root.mainloop()