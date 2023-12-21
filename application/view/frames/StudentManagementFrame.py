from tkinter import *
from tkinter import messagebox
from ..frames.BaseManagementFrame import BaseManagementFrame
from ...model.StudentModel import StudentModel
from ...view.dialog.EditDataDialog.EditIssuanceNewAccountDialog import EditIssuanceNewAccountDialog
from ...view.dialog.AddDataDialog.AddStudentDialog import AddStudentDialog
from ...view.dialog.EditDataDialog.EditStudentDialog import EditStudentDialog
from ...view.dialog.AddDataDialog.AddAccountDialog import AddAccountDialog
from ...service.StudentService import StudentService

_account1=EditIssuanceNewAccountDialog
class StudentManagementFrame(BaseManagementFrame):
    def __init__(self,master,mainScreen=None):
        super().__init__(master=master,mainScreen=mainScreen,model=StudentModel,service=StudentService,addDataDialog=AddStudentDialog,editDataDialog=EditStudentDialog,title='Quản lý học viên')
        # self.setupTitle()
        self.setupCtrlDefault()
        self.packCtrlDefault()
    def setupCtrlDefault(self, modelName=""):
        super().setupCtrlDefault(modelName)
        self.btnIssuanceAccount=Button(self.ctrlFrame,text="Cấp/đổi tài khoản",command=self.issuanceAccount)
    def packCtrlDefault(self):
        super().packCtrlDefault()
        self.btnIssuanceAccount.grid(row=2,column=0)
    def issuanceAccount(self):
        try:
            selected=self.myTable.getSelectedItem(mode='MAP')
            data={'id':selected['stid'],
                'role':'STUDENT',
                'name':selected['name'],
                'currentUsername':selected['account']
            }
            _account1(self.mainScreen,self,data).run()
        except:
            messagebox.showerror("Cấp/đổi tài khoản","Chưa chọn đối tượng!")
            return
