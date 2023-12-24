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
class ChangePasswordDialog(BaseDialog):
    def __init__(self,master,isLogin=False):
        self.isLogin=isLogin
        BaseDialog.__init__(self,master=master,title='Đổi mật khẩu',isPriority=True,isCloseMaster=True)
    def createWidgets(self):
        Label(self,text='ĐỔI MẬT KHẨU',font=_tagH1).pack(pady=10)
        usernameValue=StringVar()
        oldPasswordValue=StringVar()
        newPasswordValue=StringVar()
        confirmPasswordValue=StringVar()
        Label(self,text='Tài khoản',font=_tagH2).pack(pady=10)
        self.entryUsername=Entry(self,font=_tagH2,textvariable=usernameValue)
        self.entryUsername.pack(padx=10)
        Label(self,text='Mật khẩu cũ',font=_tagH2).pack(pady=10)
        self.entryOldPassword=Entry(self,textvariable=oldPasswordValue,font=_tagH2,show="*")
        self.entryOldPassword.pack(padx=10)
        Label(self,text='Mật khẩu mới',font=_tagH2).pack(pady=10)
        self.entryNewPassword=Entry(self,textvariable=newPasswordValue,font=_tagH2,show="*")
        self.entryNewPassword.pack(padx=10)
        Label(self,text='Xác nhận mật khẩu mới',font=_tagH2).pack(pady=10)
        self.entryConfirmPassword=Entry(self,textvariable=confirmPasswordValue,font=_tagH2,show="*")
        self.entryConfirmPassword.pack(padx=10)
        btnLogin=Button(self,text="Đổi mật khẩu",font=_tagButton,command=self.changePassword)
        btnLogin.pack(pady=10)
        if self.isLogin:
            usernameValue.set(_session().getUsername())
    def changePassword(self):
        # t=Thread(target=self.changePasswordThread)
        # t.start()
        self.changePasswordThread()
    def changePasswordThread(self):
        username=self.entryUsername.get().strip()
        oldPassword=self.entryOldPassword.get().strip()
        confirmPassword=self.entryConfirmPassword.get().strip()
        newPassword=self.entryNewPassword.get().strip()
        if  username =='' or  confirmPassword=='' or oldPassword =='' or newPassword =='':
            messagebox.showerror('Thông báo','Vui lòng nhập đầy đủ thông tin!')
            return
        if newPassword != confirmPassword:
            messagebox.showerror('Thông báo','Mật khẩu mới và xác nhận mật khẩu mới không giống nhau!')
            return
        response=_service.changePassword(username, sha256(oldPassword),sha256(newPassword))
        try:
            if response['status_code']==201:
                messagebox.showinfo("Thành công","Đổi mật khẩu thành công!")
                self.destroy()
                self.master.goToLogin()
            else:
                dictError={'invalid':'Mật khẩu cũ không chính xác',
                        'exist': 'Tài khoản không tồn tại'}
                message="Lỗi hệ thống không xác định!"
                for i in dictError.keys():
                    if i in response['message']:
                        message=dictError[i]
                        break
                    
                messagebox.showerror("Thất bại",message)
        except Exception as e:
            print(e)
            print(response)
    def cancel(self):
        super().cancel()
        if self.isLogin:
            self.master.deiconify()
        else:
            self.destroy()
            self.master.goToLogin()