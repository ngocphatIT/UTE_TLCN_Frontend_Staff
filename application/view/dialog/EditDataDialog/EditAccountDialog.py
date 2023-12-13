from ...dialog.AddDataDialog.AddAccountDialog import AddAccountDialog
from ....service.AccountService import AccountService
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
_service=AccountService()
class EditAccountDialog(AddAccountDialog):
    def __init__(self,tkMaster,master,data,title='Xin chào'):
        super().__init__(tkMaster,master,title,data)
        self.data=data
        self.dictInfoWidget['uuid']['isID']=True
        self.dictInfoWidget['username']['isID']=True
        self.dictInfoWidget['datetimeInit']['isReadOnly']=True
        self.dictInfoWidget['role']['isReadOnly']=True
    def updateData(self,data):
        for i in data.keys():
            if i in self.dictInfoWidget:
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
                
    def btnSubmitAction(self):
        myAccount=self.getDataOfForm()
        myAccount['role']=myAccount['role'].split(' - ')[1]
        response= _service.update(myAccount['uuid'],myAccount)
        print(response)
        if response['status_code']==403:
            self.master.error403()
            return
        if response['status_code']==201:
            self.master.refreshData()
            messagebox.showinfo("Thành công","Cập nhật thành công")
        else:
            messagebox.showerror("Lỗi","Định dạng dữ liệu không phù hợp")
        