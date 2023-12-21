from tkinter import *
from application.view.dialog.ServiceDialog.LoginDialog import LoginDialog
from application.view.dialog.ServiceDialog.ChangePasswordDialog import ChangePasswordDialog
from .view.screens.ManagementScreen import ManagementScreen
import sys
_loginDialog = LoginDialog
_changePasswordDialog = ChangePasswordDialog
class MyApp(Tk):
    def __init__(self):
        super().__init__()
        self.lastFrame=None
        self.currentFrame=None
        self.session={}
        self.geometry('1440x720')
        self.protocol("WM_DELETE_WINDOW",self.cancel)
        # self.resizable(0, 0)
        self.display()
    def getScreen(self,name):
        widget_list = self.winfo_children()
        for item in widget_list:
            item.pack_forget()
        dictScreen={'main':ManagementScreen}
        return dictScreen[name](self)
    def showScreen(self,name):
        self.lastFrame=self.currentFrame
        self.currentFrame=self.getScreen(name)
        if self.lastFrame is not None:
            # self.lastFrame.destroy()
            self.lastFrame.pack_forget()
        self.currentFrame.pack()
        self.currentFrame.tkraise()
    def goToChangePassword(self,isLogin=False):
        _changePasswordDialog(self,isLogin=isLogin)
    def goToLogin(self):
        _loginDialog(self)
        # self.showScreen('main')
        # pass
        
            

    def display(self):
        _loginDialog(self)
        # self.showScreen('main')

    def hidden(self):
        self.wm_withdraw()
    def comeback(self):
        self.wm_deiconify()
    def cancel(self):
        self.destroy()
        sys.exit()
    def changeSize(self,size=(1440,720)):
        self.geometry(f'{size[0]}x{size[1]}')

    def run(self):
        self.mainloop()
    