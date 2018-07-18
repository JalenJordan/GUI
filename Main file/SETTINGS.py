from tkinter import *
from tkinter import ttk
import shadows
import Antialisaing

def show():
    BLUE = (0, 0, 255)
    window = Tk()

    button = Button(window, fg ='black', text = 'Shadows', command = shadows.show2)
    button.grid(row = 1, column = 0 )


    Text = Label(window, text = 'Settings', fg = 'black')
    Text.grid(row = 0, column = 5)

    button2 = Button(window, text = "AntiAA's", command = Antialisaing.show3)
    button2.grid(row = 2, column = 0)

    button3 = Button(window, text = 'Go Back',command = window.destroy )
    button3.grid(row = 5, column = 0)
    window.mainloop()
show()

