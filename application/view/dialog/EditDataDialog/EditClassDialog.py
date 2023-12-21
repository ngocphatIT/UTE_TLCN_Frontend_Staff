from ...dialog.AddDataDialog.AddClassDialog import AddClassDialog
from ....service.ClassService import ClassService
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
_service=ClassService()
class EditClassDialog(AddClassDialog):
    def __init__(self,tkMaster,master,data,title='Chỉnh sửa thông tin lớp học'):
        super().__init__(tkMaster,master,title,data)
        self.data=data
        self.dictInfoWidget['cid']['isID']=True
    def updateData(self,data):
        for i in data.keys():
            if i in self.dictInfoWidget:
                print(i,data[i])
                if not self.dictInfoWidget[i]['type']==Combobox:
                    self.dictInfoWidget[i]['values']=data[i]
                else:
                    if i == 'isDeleted':
                        if data[i]=='True':
                            data[i] = True
                        elif data[i]=='False':
                            data[i] = False
                        self.dictInfoWidget[i]['currentChoice']=self.dictInfoWidget[i]['values'].index(data[i])
                    else:
                        index=-1
                        for j in range(len(self.dictInfoWidget[i]['values'])):
                            if data[i] in self.dictInfoWidget[i]['values'][j]:
                                index=j
                                break
                        if index!=-1:
                            self.dictInfoWidget[i]['currentChoice']=index
    def submitActionThread(self):
        myClass=self.getDataOfForm()
        myClass['course']=myClass['course'].split(' - ')[1]
        response=_service.update(myClass['cid'],myClass)
        self.isWaiting=False
        self.isWaiting=False
        if response['status_code']==403:
            self.master.error403()
            return
        if response['status_code']==201:
            self.master.refreshData()
            messagebox.showinfo("Thành công","Thêm thành công!")
        else:
            messagebox.showerror("Lỗi","Trùng mã đối tượng")
                

        
        