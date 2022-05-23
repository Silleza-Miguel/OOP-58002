from tkinter import *

window = Tk()
window.geometry("300x300")
window.title('Finals Exam')


class GUI:
    def __init__(self, window):
        self.L = []

        self.label = Label(window, text="Find the least number among three numbers")
        self.label.pack(side=TOP, pady=40)

        self.entry1 = Entry(window, bd=3)
        self.entry1.place(x=150, y=100)
        self.entrylbl1 = Label(window, text="First Number")
        self.entrylbl1.place(x=40, y=100)

        self.entry2 = Entry(window, bd=3)
        self.entry2.place(x=150, y=145)
        self.entrylbl2 = Label(window, text="Second Number")
        self.entrylbl2.place(x=40, y=145)

        self.entry3 = Entry(window, bd=3)
        self.entry3.place(x=150, y=190)
        self.entrylbl3 = Label(window, text="Third Number")
        self.entrylbl3.place(x=40, y=190)

        self.button = Button(window, text="Find", padx=5, command=self.display)
        self.button.place(x=90, y=235)
        self.output = Entry(window, bd=3)
        self.output.place(x=150, y=235)

    def display(self):
        self.output.delete(0, "end")
        self.L.clear()

        self.L.append(self.entry1.get())
        self.L.append(self.entry2.get())
        self.L.append(self.entry3.get())
        self.output.insert(END, min(self.L))


mywin = GUI(window)

window.mainloop()

