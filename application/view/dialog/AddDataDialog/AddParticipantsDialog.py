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
    def __init__(self,tkMaster,master,title='Thêm thành viên lớp học',data=None,model=ParticipantsClassModel,service=ClassService,classID=''):
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
    def submitActionThread(self):
        obj=self.getDataOfForm()
        response=self.service.addParticipants(self.classID,obj)
        self.isWaiting=False
        if response['status_code']==403:
            self.master.error403()
            return
        if response['status_code']==201:
            self.master.refreshData()
            messagebox.showinfo("Thành công","Thêm thành công!")
        elif response['status_code']==404:
            messagebox.showerror("Lỗi","Không tìm thấy thành viên")
        else:
            messagebox.showerror("Lỗi","Thành viên đã có trong lớp học")