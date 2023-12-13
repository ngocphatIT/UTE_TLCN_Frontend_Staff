from tkinter import *
from tkinter import messagebox

class BaseDialog(Toplevel):
    def __init__(self,master,title,isCloseMaster=False,isPriority=False):
        Toplevel.__init__(self,master)
        self.title(title)
        if isCloseMaster:
            self.master.wm_withdraw()
        if isPriority and not isCloseMaster:
            self.transient(master)
        self.protocol("WM_DELETE_WINDOW",self.cancel)
        self.createWidgets()
        self.grab_set()
        self.wait_window()
    def createWidgets(self):
        pass
    def cancel(self):
        self.destroy()