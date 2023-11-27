from tkinter import *

_tagH1=('Arial',20,'bold')
_tagH2=('Arial',18)
_tagButton=('Arial',18)
class StudentScreen(Frame):
    def __init__(self,master):
        Frame.__init__(self)    
        Label(self,text='CHÀO MỪNG',font=_tagH1).pack(pady=10)
        self.master=master
        # usernameValue=StringVar()
        # passwordValue=StringVar()
        # Label(self,text='Username',font=_tagH2).pack(pady=10)
        # entryUsername=Entry(self,font=_tagH2,textvariable=usernameValue)
        # entryUsername.pack(padx=10)
        # Label(self,text='Password',font=_tagH2).pack(pady=10)
        # entryPassword=Entry(self,textvariable=passwordValue,font=_tagH2,show="*")
        # entryPassword.pack(padx=10)
        btnLogin=Button(self,text="Login",font=_tagButton)
        btnLogin.pack(pady=10)
    def next(self):
        self.master.showScreen('student')