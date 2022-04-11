from tkinter import *


class Window:
    def __init__(self,win):
        self.label = Label(win, text="Enter your full name", fg="red").place(x=50, y=50)
        self.button = Button(win, text="Click here to display your name", command=self.display, fg="red").place(x=50, y=100)
        self.textfield = Entry(bd=5)
        self.textfield2 = Entry(bd=5)
        self.textfield.place(x=275, y=50, width=150)
        self.textfield2.place(x=275, y= 100, width=150)

    def display(self):
        self.textfield2.delete(0, END)
        name = self.textfield.get()
        self.textfield2.insert(END, f"{name}")


win = Tk()
win.title("Midterms OOP")
win.geometry("450x200")
root = Window(win)
win.mainloop()