from tkinter import *
from tkinter.ttk import *
from tkcalendar import Calendar,DateEntry
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from ...dialog.AddDataDialog.BaseAddDialog import BaseAddDialog
from ....model.ParticipantsClassModel import ParticipantsClassModel
from ....service.ClassService import ClassService


from datetime import date


today = str(date.today())

class AddParticipantsDialog(BaseAddDialog):
    def __init__(self,tkMaster,master,title='Xin chào',data=None,model=ParticipantsClassModel,service=ClassService,classID=''):
        self.classID=classID
        super().__init__(tkMaster,master,title,data,model,service)
        
        roleList=['STUDENT','LECTURER']
        self.dictInfoWidget = {'id':{
            'type':Entry,
            'typeData':StringVar(),
            'width':5
        },
        'role':
        {
            'type':Combobox,
            'typeData':StringVar(),
            'values':roleList,
            'currentChoice':0,
            'isReadOnly':True,
            'width':20
        }
        }
    def btnSubmitAction(self):
        obj=self.getDataOfForm()
        print(obj)
        response=self.service.addParticipants(self.classID,obj)
        if response['status_code']==403:
            self.master.error403()
            return
        if response['status_code']==201:
            self.master.refreshData()
            messagebox.showinfo("Thành công","Thêm thành công!")
        else:
            messagebox.showerror("Lỗi",response['message'])