from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from ...dialog.AddDataDialog.BaseAddDialog import BaseAddDialog
from ....model.CourseModel import CourseModel
from ....service.CourseService import CourseService
from ....service.CourseCategoryService import CourseCategoryService
class AddCourseDialog(BaseAddDialog):
    def __init__(self,tkMaster,master,title='Thêm khóa học',data=None,model=CourseModel,service=CourseService):
        super().__init__(tkMaster,master,title,data,model,service)
        cat=CourseCategoryService().getAll()['message']
        catValue=[]
        for i in cat:
            if 'isDeleted' not in i:
                i['isDeleted']=False
            if not i['isDeleted']:
                catValue.append(f"{i['nameCategory']} - {i['cid']}")
        self.dictInfoWidget = {'cid':{
            'type':Entry,
            'typeData':StringVar()
        },
        'courseName':{
            'type':Entry,
            'typeData':StringVar(),
        },
        'category':
        {
            'type':Combobox,
            'typeData':StringVar(),
            'values':catValue,
            'currentChoice':0,
            'isReadOnly':True,
            'width':20
        },
        'description':{
            'type':Entry,
            'typeData':StringVar(),
        },
        }
    def submitActionThread(self):
        course=self.getDataOfForm()
        course['category']=course['category'].split(' - ')[1]
        response=self.service.create(course)
        if response['status_code']==403:
            self.master.error403()
            return
        self.isWaiting=False
        if response['status_code']==201:
            self.master.refreshData()
            messagebox.showinfo("Thành công","Thêm thành công!")
        else:
            messagebox.showerror("Lỗi","Trùng mã đối tượng")