from ....service.AuthenticationService import AuthenticationService
from .BaseDialog import BaseDialog
from tkinter import *
from tkinter import messagebox
from ....myLib.myCrypto import sha256
from ....service.SQLLiteService import SessionDataService
from threading import *
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
        Label(self,text='Tên đăng nhập',font=_tagH2).pack(pady=10)
        self.entryUsername=Entry(self,font=_tagH2,textvariable=usernameValue)
        self.entryUsername.pack(padx=10)
        Label(self,text='Mật khẩu',font=_tagH2).pack(pady=10)
        self.entryPassword=Entry(self,textvariable=passwordValue,font=_tagH2,show="*")
        self.entryPassword.pack(padx=10)
        btnLogin=Button(self,text="Đăng nhập",font=_tagButton,command=self.login)
        btnLogin.pack(pady=10)
        btnChangePassword=Button(self,text="Đổi mật khẩu",font=_tagButton,command=self.goToChangePassword)
        btnChangePassword.pack(pady=10)
        self.result={'isLogin':False,'message':""}
    def login(self):
        self.loginThread()
    def goToChangePassword(self):
        self.destroy()
        self.master.goToChangePassword()
    def loginThread(self):
        username=self.entryUsername.get()
        password=self.entryPassword.get()
        response=_service.login(username,sha256(password) )
        try:
            if 'Authorization' in response['message']:
                self.result={'Authorization': response['message']['Authorization'],'isLogin':True}
                _session().setAuthorization(response['message']['Authorization'])
                _session().setUsername(username)
                self.destroy()
                self.master.deiconify()
                self.master.showScreen('main')
            else:
                if 'username' in response['message']:
                    message='Tài khoản hoặc mật khẩu không chính xác!'
                else:
                    message="Lỗi hệ thống không xác định!"
                messagebox.showerror("Thất bại",message)
        except Exception as e:
            print(e)
            print(response)
    def cancel(self):
        super().cancel()
        self.destroy()