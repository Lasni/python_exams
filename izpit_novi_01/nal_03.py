from tkinter import *


def convert():
    try:
        n = float(e.get())
        x = n * 239.64
        e.delete(0, END)
        e.insert(END, str(x))
    except:
        e.delete(0, END)
        e.insert(END, "Error. Need a number.")

root = Tk()

l = Label(root, text="Currency converter")
l.pack()

e = Entry(root, width=20)
e.pack()

b = Button(root, text="Convert", command=convert)
b.pack()


root.mainloop()


