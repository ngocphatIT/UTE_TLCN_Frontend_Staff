from tkinter import *
from application.view.dialog.ServiceDialog.LoginDialog import LoginDialog
from .view.screens.ManagementScreen import ManagementScreen
from application.service.SQLLiteService import SessionDataService
_loginDialog = LoginDialog
_session=SessionDataService
from application.view.dialog.ViewDialog.ViewClassParticipantsDialog import ViewParticipantsDialog
class MyApp(Tk):
    def __init__(self):
        super().__init__()
        self.lastFrame=None
        self.currentFrame=None
        self.session={}
        self.geometry('1440x720')
        self.protocol("WM_DELETE_WINDOW",self.destroy)
        self.display()
    def getScreen(self,name):
        dictScreen={
                    'main':ManagementScreen}
        return dictScreen[name](self)
    def showScreen(self,name):
        self.lastFrame=self.currentFrame
        self.currentFrame=self.getScreen(name)
        if self.lastFrame is not None:
            self.lastFrame.pack_forget()
        self.currentFrame.pack()
        self.currentFrame.tkraise()
    def goToLogin(self):
        _loginDialog(self)
        # self.showScreen('main')
        # pass
        
            

    def display(self):
        self.showScreen('main')

    def hidden(self):
        self.wm_withdraw()
    def comeback(self):
        self.wm_deiconify()

    def run(self):
        self.mainloop()
    