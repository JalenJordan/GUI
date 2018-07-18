from tkinter import *
   
def show3():
    window4 = Tk()

    percent = Label(window4, text = ' AA percentage')
    percent.pack()
    var = DoubleVar()
    selection = "Value = " + str(var.get())
    scale = Scale( window4, variable = var )
    scale.pack(anchor=CENTER)
    button = Button(window4, text="Get Scale Value")

    button2 = Button(window4, text = 'Go back', command = window4.destroy)
    button2.pack()

    label = Label(window4)
    label.pack()
    label.config(text = selection)

    window4.mainloop()




