# reference: https://stackoverflow.com/questions/58006764/is-there-a-way-to-ask-for-multiple-choices-in-a-popup-like-messagebox-do
from tkinter import *
from tkinter import messagebox
from .BaseDialog import BaseDialog
class OptionDialog(BaseDialog):
    def __init__(self,parent,title,question,options):
        self.question = question
        self.options = options
        self.result = '_'
        BaseDialog.__init__(self,parent,title)
    def createWidgets(self):
        frmQuestion = Frame(self)
        Label(frmQuestion,text=self.question).grid()
        frmQuestion.grid(row=1)
        frmButtons = Frame(self)
        frmButtons.grid(row=2)
        column = 0
        for option in self.options:
            btn = Button(frmButtons,text=option,command=lambda x=option:self.setOption(x))
            btn.grid(column=column,row=0,padx=10,pady=10)
            column += 1 
    def setOption(self,optionSelected):
        self.result = optionSelected
        self.destroy()
    def cancel(self):
        self.result = None
        self.destroy()
