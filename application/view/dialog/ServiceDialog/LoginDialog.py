from ....service.AuthenticationService import AuthenticationService
from .BaseDialog import BaseDialog
from tkinter import *
from tkinter import messagebox
from ....service.SQLLiteService import SessionDataService
_session=SessionDataService
_service=AuthenticationService()
_tagH1=('Arial',20,'bold')
_tagH2=('Arial',18)
_tagButton=('Arial',18)
class LoginDialog(BaseDialog):
    def __init__(self,master):
        BaseDialog.__init__(self,master=master,title='Đăng nhập',isPriority=True,isCloseMaster=True)
    def createWidgets(self):
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
        self.result={'isLogin':False,'message':""}
    def login(self):
        response=_service.login(self.entryUsername.get(), self.entryPassword.get())
        try:
            if 'Authorization' in response['message']:
                self.result={'Authorization': response['message']['Authorization'],'isLogin':True}
                _session().setAuthorization(response['message']['Authorization'])
                self.destroy()
                self.master.deiconify()
                self.master.showScreen('main')

            else:
                messagebox.showinfo(self.title,response['message'])
        except Exception as e:
            print(e)
            print(response)
    def cancel(self):
        super().cancel()
        self.master.destroy()