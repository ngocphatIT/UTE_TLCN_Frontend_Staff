from ...dialog.AddDataDialog.AddCourseCategoryDialog import AddCourseCategoryDialog
from ....service.CourseCategoryService import CourseCategoryService
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
_service=CourseCategoryService()
class EditCourseCatoryDialog(AddCourseCategoryDialog):
    def __init__(self,tkMaster,master,data,title='Xin chào'):
        super().__init__(tkMaster,master,title,data)
        self.data=data
        self.dictInfoWidget['cid']['isReadOnly']=True
    def updateData(self,data):
        for i in data.keys():
            if not self.dictInfoWidget[i]['type']==Combobox:
                self.dictInfoWidget[i]['values']=data[i]
            else:
                if data[i]=='True':
                    data[i] = True
                elif data[i]=='False':
                    data[i] = False
                self.dictInfoWidget[i]['currentChoice']=self.dictInfoWidget[i]['values'].index(data[i])
    def btnSubmitAction(self):
        category=self.getDataOfForm()
        if 'cid' in _service.update(category['cid'],category)[0] :
            self.master.refreshData()
            messagebox.showinfo("Thành công","Cập nhật thành công")
        else:
            messagebox.showerror("Lỗi","Định dạng dữ liệu không phù hợp")
        