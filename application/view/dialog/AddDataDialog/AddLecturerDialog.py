from tkinter import *
from tkinter.ttk import *
from tkcalendar import Calendar,DateEntry
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from ...dialog.AddDataDialog.BaseAddDialog import BaseAddDialog
from ....model.LecturerModel import LecturerModel

from ....service.LecturerService import LecturerService
from ....service.TypePersonalIDService import TypePersonalIDService
from datetime import date


today = str(date.today())

_typePersonService=TypePersonalIDService()
class AddLecturerDialog(BaseAddDialog):
    def __init__(self,tkMaster,master,title='Thêm giảng viên',data=None,model=LecturerModel,service=LecturerService):
        super().__init__(tkMaster,master,title,data,model,service)
        typePersonal=_typePersonService.getAll()['message']
        typePersonalValue=[]
        for i in typePersonal:
            typePersonalValue.append(f"{i['name']} - {i['tpid']}")
        self.dictInfoWidget = {'lid':{
            'type':Entry,
            'typeData':StringVar()
        },
        'name':{
            'type':Entry,
            'typeData':StringVar(),
        },
        'personID':{
            'type':Entry,
            'typeData':StringVar(),
        },
        'typePersonID':
        {
            'type':Combobox,
            'typeData':StringVar(),
            'values':typePersonalValue,
            'currentChoice':0,
            'isReadOnly':True,
            'width':20
        },
        'datetimeInit':{
            'type':Entry,
            'typeData':StringVar(),
            'values':today,
            'isReadOnly':True
        }
        }
    def submitActionThread(self):
        lecturer=self.getDataOfForm()
        del lecturer['datetimeInit']
        lecturer['typePersonID']=lecturer['typePersonID'].split(' - ')[1]
        response=self.service.create(lecturer)
        self.isWaiting=False
        if response['status_code']==403:
            self.master.error403()
            return
        if response['status_code']==201:
            self.master.refreshData()
            messagebox.showinfo("Thành công","Thêm thành công!")
        else:
            messagebox.showerror("Lỗi","Trùng mã đối tượng")