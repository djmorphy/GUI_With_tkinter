from tkinter import *

root = Tk()
# e = Entry(root, width=50, bg="gray", fg="white", borderwidth=5)
# e.pack()
e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter your name: ")  #placeholder
def myClick():
    # myLabel = Label(root, text="Look! I clicked a Button!")
    hello = "Hello " + e.get()
    # myLabel = Label(root, text="Hello "+ e.get())
    myLabel = Label(root, text=hello)
    myLabel.pack()

myButton = Button(root, text="Enter your name", command=myClick)
myButton.pack()

root.mainloop()