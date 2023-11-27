from tkinter import *
from tkinter import messagebox
from ...service.AuthenticationService import AuthenticationService
_tagH1=('Arial',20,'bold')
_tagH2=('Arial',18)
_tagButton=('Arial',18)
class LoginScreen(Frame):
    def __init__(self,master):
        Frame.__init__(self)
        self.title='Đăng nhập'
        self.master = master    
        Label(self,text='CHÀO MỪNG',font=_tagH1).pack(pady=10)
        usernameValue=StringVar()
        passwordValue=StringVar()
        Label(self,text='Username',font=_tagH2).pack(pady=10)
        self.entryUsername=Entry(self,font=_tagH2,textvariable=usernameValue)
        self.entryUsername.pack(padx=10)
        Label(self,text='Password',font=_tagH2).pack(pady=10)
        self.entryPassword=Entry(self,textvariable=passwordValue,font=_tagH2,show="*")
        self.entryPassword.pack(padx=10)
        btnLogin=Button(self,text="Login",font=_tagButton,command=self.login)
        btnLogin.pack(pady=10)
        # self.master.title=self.title
    def login(self):
        response=AuthenticationService().login(self.entryUsername.get(), self.entryPassword.get())

        # print(response['Authorization'])
        try:
            # if 'Authorization' in response:
                # self.master.session['Authorization']=response['Authorization']
                self.master.showScreen('main')
                print('ok')
                return 
        except Exception as e:
            print(e)
            print(response)
        messagebox.showinfo(self.title,"Thông tin không chính xác")