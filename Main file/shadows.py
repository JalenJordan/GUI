from tkinter import *
   
def show2():
    window3 = Tk()

    percent = Label(window3, text = ' shadows percentage')
    percent.pack()
    var = DoubleVar()
    selection = "Value = " + str(var.get())
    scale = Scale( window3, variable = var )
    scale.pack(anchor=CENTER)
    button = Button(window3, text="Get Scale Value")

    button2 = Button(window3, text = 'Go back', command = window3.destroy)
    button2.pack()

    label = Label(window3)
    label.pack()
    label.config(text = selection)

    window3.mainloop()