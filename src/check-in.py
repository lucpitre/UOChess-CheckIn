from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image
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

    #create widgets for ui
    def createWidgets(self):
        self.entry = Entry(self.tk, width=10)
        self.btn = Button(self.tk, text="Submit", command=self.submitCheckin)
        self.lblText = StringVar()
        self.label = Label(self.tk, textvariable=self.lblText)
        self.img = ImageTk.PhotoImage(Image.open('../assets/Transparent_Logo.png'))
        self.logo = Label(self.tk, image=self.img)
        
        self.logo.pack(side = "bottom", fill = "both", expand = "yes")

        self.entry.pack()
        self.btn.pack()
        self.label.pack()

    #submit checkin
    def submitCheckin(self, event=None):
        self.studentNo = int(self.entry.get()) #get student number from text box
        self.studentName = memberExists(self.studentNo) #check if student is in database

        if self.studentName != False: #if studentName is false, student is not signed up
            self.lblText.set(self.studentName)
            addVisit(self.studentNo) #add visit for the student
    
    #toggle fullscreen
    def toggle_fullscreen(self, event=None):
        self.state = not self.state  #toggling the boolean
        self.tk.attributes("-fullscreen", self.state) #set status of fullscreen to toggled boolean
        return "break"

    #end fullscreen
    def end_fullscreen(self, event=None):
        self.state = False #update boolean tracking fullscreen
        self.tk.attributes("-fullscreen", False) #turn of fullscreen
        return "break"



w = Check_In()
w.tk.mainloop()