from tkinter import *

root = Tk()

label = Label(root, text="nal_04")
label.pack()

txtarea = Entry(root, width=50)
txtarea.pack()


def zapisi():
    s = txtarea.get()
    outfile = open("nal_04.txt", "a")
    outfile.write(s+"\n")
    outfile.close()

btn = Button(root, text="zapisi", command=zapisi)
btn.pack()

root.mainloop()
