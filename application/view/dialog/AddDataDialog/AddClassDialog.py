from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkcalendar import Calendar,DateEntry

from ...dialog.AddDataDialog.BaseAddDialog import BaseAddDialog
from ....model.ClassModel import ClassModel

from ....service.ClassService import ClassService
from ....service.CourseService import CourseService
from datetime import date

today = str(date.today())
_service=ClassService()
_courseService=CourseService()
class AddClassDialog(BaseAddDialog):
    def __init__(self,tkMaster,master,title='Thêm lớp',data=None,model=ClassModel,service=ClassService):
        super().__init__(tkMaster,master,title,data,model,service)
        course=_courseService.getAll()['message']
        courseValue=[]
        for i in course:
            if not i['isDeleted']:
                courseValue.append(f"{i['courseName']} - {i['cid']}")
        self.dictInfoWidget = {'cid':{
            'type':Entry,
            'typeData':StringVar()
        },
        'className':{
            'type':Entry,
            'typeData':StringVar(),
        },
        'course':
        {
            'type':Combobox,
            'typeData':StringVar(),
            'values':courseValue,
            'currentChoice':0,
            'isReadOnly':True,
            'width':20
        },
        'dateStart':
        {
            'type':DateEntry,
            'typeData':StringVar(),
            'values':today,
            'isReadOnly':True,
            'config':{'date_pattern':'yyyy-mm-dd'}
        },
        'dateEnd':
        {
            'type':DateEntry,
            'typeData':StringVar(),
            'isReadOnly':True,
            'values':today,
            'config':{'date_pattern':'yyyy-mm-dd'}
        },
        'description':{
            'type':Entry,
            'typeData':StringVar(),
        }}
    def submitActionThread(self):
        myClass=self.getDataOfForm()
        myClass['course']=myClass['course'].split(' - ')[1]
        print(myClass)
        response=_service.create(myClass)
        self.isWaiting=False
        if response['status_code']==403:
            self.master.error403()
            return
        if response['status_code']==201:
            self.master.refreshData()
            messagebox.showinfo("Thành công","Thêm thành công!")
        else:
            messagebox.showerror("Lỗi","Trùng mã đối tượng")