from tkinter import *
from tkinter.ttk import *

class Check_In:

    def __init__(self):
        self.tk = Tk()
        self.tk.title("UOChess Check-In")

root = Tk()
root.title("UOChess Check-In")
root.attributes('-fullscreen', True)

label = Label(root, text ="Hello World !").pack()

studentNo = Entry(root, width=10)
#studentNo.grid(column=1, row=0)

root.mainloop()
