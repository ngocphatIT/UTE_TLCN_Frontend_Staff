from tkinter import *

_tagH1=('Arial',20,'bold')
_tagH2=('Arial',18)
_tagButton=('Arial',18)
class ClassScreen(Frame):
    def __init__(self,master):
        Frame.__init__(self)    
        self.master=master
        Label(self,text='CHÀO MỪNG tasgasdf asdfagegwfjadsgyaqy d ad fsd',font=_tagH1).pack(pady=10)
        # usernameValue=StringVar()
        # passwordValue=StringVar()
        # Label(self,text='Username',font=_tagH2).pack(pady=10)
        # entryUsername=Entry(self,font=_tagH2,textvariable=usernameValue)
        # entryUsername.pack(padx=10)
        # Label(self,text='Password',font=_tagH2).pack(pady=10)
        # entryPassword=Entry(self,textvariable=passwordValue,font=_tagH2,show="*")
        # entryPassword.pack(padx=10)
        btnLogin=Button(self,text="Login",font=_tagButton,command=self.next)
        btnLogin.pack(pady=10)
    def next(self):
        self.master.showScreen('login')