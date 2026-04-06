from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("User Form")
root.geometry("500x400")

def submit():
    name = e1.get()
    messagebox.showinfo("Output", "Hello " + name)

e1 = Entry(root)
e1.place(x=100, y=100)

btn = Button(root, text="Submit", command=submit)
btn.place(x=100, y=150)

root.mainloop()
