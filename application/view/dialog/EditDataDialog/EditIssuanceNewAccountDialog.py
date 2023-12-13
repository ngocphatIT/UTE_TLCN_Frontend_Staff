from ...dialog.AddDataDialog.AddIssuanceNewAccountDialog import AddIssuanceNewAccountDialog
from ....service.AccountService import AccountService
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
_service=AccountService()
class EditIssuanceNewAccountDialog(AddIssuanceNewAccountDialog):
    def __init__(self,tkMaster,master,data,title='Xin chào'):
        super().__init__(tkMaster,master,title,data)
        self.data=data
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
                            print(self.dictInfoWidget[i]['values'][j])
                            if data[i] in self.dictInfoWidget[i]['values'][j]:
                                index=j
                                break 
                        if index!=-1:
                            self.dictInfoWidget[i]['currentChoice']=index
        self.dictInfoWidget['role']['isReadOnly']=True
        self.dictInfoWidget['role']['isID']=True
                
    def btnSubmitAction(self):
        account=self.getDataOfForm()
        account['role']=account['role'].split(' - ')[1]
        
        account['id']=int(account['id'])
        if account['currentUsername'] != account['username']:
            del account['name']
            del account['currentUsername']
            response=_service.inssuanceNewAccount(account)
            if response['status_code']==403:
                self.master.error403()
                return
            if response['status_code']==201:
                    self.master.refreshData()
                    messagebox.showinfo("Thành công","Cấp thành công")
                    return
            messagebox.showerror("Lỗi",response['message'])
            return
        messagebox.showerror("Trùng dữ liệu","Tên đăng nhập mới phải khác tên đăng nhập hiện tại")
        