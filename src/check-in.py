from tkinter import *
from tkinter.ttk import *

class Check_In:

    def __init__(self):
        self.tk = Tk()
        self.tk.title("UOChess Check-In")
        self.tk.attributes('-fullscreen', True)

        self.state = True

        self.tk.bind("<F11>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.end_fullscreen)
    
    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.tk.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.tk.attributes("-fullscreen", False)
        return "break"


#label = Label(root, text ="Hello World !").pack()

#studentNo = Entry(root, width=10)
#studentNo.grid(column=1, row=0)

w = Check_In()
w.tk.mainloop()