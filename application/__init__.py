from tkinter import *
from application.view.screens.LoginScreen import LoginScreen
from application.view.screens.ClassScreen import ClassScreen
from .view.screens.ManagementScreen import ManagementScreen

class MyApp(Tk):
    def __init__(self):
        super().__init__()
        self.lastFrame=None
        self.currentFrame=None
        self.session={}
        self.geometry('1440x720')
        self.display()
    def getScreen(self,name):
        dictScreen={'login':LoginScreen,
                    'class':ClassScreen,
                    'main':ManagementScreen}
        return dictScreen[name](self)
    def showScreen(self,name):
        self.lastFrame=self.currentFrame
        self.currentFrame=self.getScreen(name)
        if self.lastFrame is not None:
            self.lastFrame.pack_forget()
        self.currentFrame.pack()
        self.currentFrame.tkraise()
    def waitingResponse(self,title='Chờ phản hồi',message='Vui lòng chờ!'):
        messagebox = Toplevel(self)
        messagebox.title(title)
        messagebox.resizable(False, False)
        label = Label(messagebox, text=message)
        label.pack()
        def on_timeout():
            from .config import myConfig
            if not myConfig.getIS_WAITING_RESPONSE():
                self.wm_deiconify()
                print("fine")
                messagebox.destroy()
        self.after(100,on_timeout)
        self.wm_withdraw()
        messagebox.mainloop()
    def display(self):
        self.showScreen('main')
    def hidden(self):
        self.wm_withdraw()
    def comeback(self):
        self.wm_deiconify()

    def run(self):
        self.mainloop()
    