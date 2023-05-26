from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look! I clicked a Button")
    myLabel.pack()

myButton = Button(root, text="Click me1!", state=DISABLED)#state disable hogy inaktiv a gomb
myButton = Button(root, text="Click me2!", padx=50, pady=50, command=myClick, fg="blue", bg="green") #meretezes es execute myClick. Lehet fg/bg hex is
myButton.pack()

root.mainloop()