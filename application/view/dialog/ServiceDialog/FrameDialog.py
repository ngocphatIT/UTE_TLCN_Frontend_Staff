from .BaseDialog import BaseDialog
from tkinter import Frame
class FrameDialog(BaseDialog):
    def __init__(self,master,title,frame):
        BaseDialog.__init__(self,master,title)
        self.frame=frame
        self.frame.master=self
        # print(self.frame.master)
        self.frame.pack()
        self.frame.tkraise()
        print(self.frame)
    