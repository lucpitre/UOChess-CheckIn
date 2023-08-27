from tkinter import *
from tkinter.ttk import *
from data import *

class Check_In:

    def __init__(self):
        self.tk = Tk()
        self.tk.title("UOChess Check-In")
        self.tk.attributes('-fullscreen', True)

        self.state = True
        self.validCheckin = False
        self.studentNo = 0

        self.createWidgets()

        self.tk.bind('<Return>', self.submitCheckin)
        self.tk.bind('<F11>', self.toggle_fullscreen)
        self.tk.bind('<Escape>', self.end_fullscreen)

    def createWidgets(self):
        self.entry = Entry(self.tk, width=10)
        self.entry.pack()
        self.btn = Button(self.tk, text="Submit", command=self.submitCheckin).pack()
        self.lblText = StringVar()
        self.label = Label(self.tk, textvariable=self.lblText).pack()

    def submitCheckin(self, event=None):
        self.studentNo = int(self.entry.get())
        self.validCheckin = memberExists(self.studentNo)

        if self.validCheckin != False:
            self.lblText.set(self.validCheckin)
    
    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.tk.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.tk.attributes("-fullscreen", False)
        return "break"



w = Check_In()
w.tk.mainloop()