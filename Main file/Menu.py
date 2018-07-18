from tkinter import *
import SETTINGS

def change():
    SETTINGS.show()

window2 = Tk()

Menu = Label(window2, text = 'Menu', fg = 'black')
Menu.grid(row = 0, column = 5)

setting = Button(window2, text = 'Settings', command=change)
setting.grid(row = 5, column = 5)



window2.mainloop()