from tkinter import *

root = Tk()

#creating label widget
# myLabel1 = Label(root, text="Hello World")
# myLabel2 = Label(root, text="My name is djmorphy")
# myLabel3 = Label(root, text="I like coffee")

#shoving it onto the screen

# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1, column=0)
# myLabel3.grid(row=1, column=1)

#oop miatt
myLabel1 = Label(root, text="Hello World").grid(row=0, column=0)
myLabel2 = Label(root, text="My name is djmorphy").grid(row=1, column=0)
myLabel3 = Label(root, text="I like coffee").grid(row=1, column=1)
root.mainloop()