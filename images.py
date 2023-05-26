from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title("Leanr Code")
root.iconbitmap('icon.ico')

my_image = ImageTk.PhotoImage(Image.open("amerika.jpg"))
mylabel = Label(image=my_image)
mylabel.pack()



button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()