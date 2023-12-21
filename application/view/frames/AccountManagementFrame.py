from ..frames.BaseManagementFrame import BaseManagementFrame
from tkinter import *
from tkinter import messagebox
from ...service.AccountService import AccountService
from ...model.AccountModel import AccountModel
from ..dialog.AddDataDialog.AddAccountDialog import AddAccountDialog
from ..dialog.EditDataDialog.EditAccountDialog import EditAccountDialog
from ..dialog.ServiceDialog.OptionDialog import OptionDialog
class AccountManagementFrame(BaseManagementFrame):
    def __init__(self,master,mainScreen=None):
        super().__init__(master=master,mainScreen=mainScreen,model=AccountModel,service=AccountService,addDataDialog=AddAccountDialog,editDataDialog=EditAccountDialog,title='Quản lý tài khoản')
        # self.setupTitle()
        self.setupCtrlDefault()
        self.packCtrlDefault()
        self.btnAdd.config(state='disabled')
    def setupCtrlDefault(self, modelName=""):
        super().setupCtrlDefault(modelName)
        # self.btnNewPassword=Button(self.ctrlFrame,text="Cấp lại mật khẩu",command=self.btnNewPasswordAction)
    def deletedActionThread(self):
        try:
            selected=self.myTable.getSelectedItem(mode='MAP')
            options=['Xóa tài khoản','Xóa quyền']
            answer=OptionDialog(self.mainScreen,'Xóa',f'''Chọn chế độ xóa đối với tài khoản '{selected["username"]}' có quyền '{selected["role"]}'  ''',options).result
            print(answer)
            if answer is not None:
                if options.index(answer)==0:
                    res=messagebox.askquestion('Xóa', f'''Bạn có chắc chắn muốn xóa tài khoản '{selected['username']}' không?''')
                    if res == 'yes':
                        if self.service.delete(selected['uuid'])['status_code']==201:
                            messagebox.showinfo('Thành công','Xóa thành công')
                            self.refreshData()
                        else:
                            messagebox.showerror('Lỗi', 'Vui lòng thử lại')
                else:
                    res=messagebox.askquestion('Xóa', f'''Bạn có chắc chắn muốn xóa quyền '{selected['role']}' tài khoản '{selected['username']}' không?''')
                    if res=='yes':
                        response=self.service.deleteRole(selected['uuid'],selected['role'])
                        if response['status_code']==201:
                            messagebox.showinfo('Thành công','Xóa thành công')
                            self.refreshData()
                        else:
                            messagebox.showerror('Lỗi', 'Vui lòng thử lại')
        except Exception as e:
            print(e)
            messagebox.showerror("Xóa","Chưa chọn đối tượng!")
        self.isWaiting=False

