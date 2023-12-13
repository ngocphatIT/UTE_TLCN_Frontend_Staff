from tkinter import Toplevel,Label
from ...frames.ViewParticipantsFrame import ViewParticipantsFrame
class ViewParticipantsDialog(Toplevel):
    def __init__(self,master,classID,className):
        super().__init__(master)
        self.master = master
        self.frame=ViewParticipantsFrame(self,self.master,classID,className)
        self.frame.packFrame()
        self.frame.tkraise()    
