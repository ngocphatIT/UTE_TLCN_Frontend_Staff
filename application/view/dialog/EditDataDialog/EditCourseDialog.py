from ...dialog.AddDataDialog.AddCourseDialog import AddCourseDialog
from ....service.CourseService import CourseService
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
_service=CourseService()
class EditCourseDialog(AddCourseDialog):
    def __init__(self,tkMaster,master,data,title='Chỉnh sửa thông tin khóa học'):
        super().__init__(tkMaster,master,title,data)
        self.data=data
        self.dictInfoWidget['cid']['isID']=True
    def updateData(self,data):
        for i in data.keys():
            if i in self.dictInfoWidget:
                if not self.dictInfoWidget[i]['type']==Combobox:
                    self.dictInfoWidget[i]['values']=data[i]
                else:
                    if data[i]=='True':
                        data[i] = True
                    elif data[i]=='False':
                        data[i] = False
                    self.dictInfoWidget[i]['currentChoice']=self.dictInfoWidget[i]['values'].index(data[i])
    def submitActionThread(self):
        category=self.getDataOfForm()
        response=_service.update(category['cid'],category) 
        if response['status_code']==403:
            self.master.error403()
            return
        if response['status_code']==201:
            self.master.refreshData()
            messagebox.showinfo("Thành công","Cập nhật thành công")
        else:
            messagebox.showerror("Lỗi","Định dạng dữ liệu không phù hợp")
        