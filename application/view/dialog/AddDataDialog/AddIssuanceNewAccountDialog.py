from tkinter import *
from tkinter.ttk import *

from ...dialog.AddDataDialog.BaseAddDialog import BaseAddDialog
from ....model.IssuanceNewAccountModel import IssuanceNewAccountModel

from ....service.AccountService import AccountService
from datetime import date

today = str(date.today())
class AddIssuanceNewAccountDialog(BaseAddDialog):
    def __init__(self,tkMaster,master,title='Cấp tài khoản',data=None,model=IssuanceNewAccountModel,service=AccountService,role='STUDENT'):
        super().__init__(tkMaster,master,title,data,model,service)
        self.dictInfoWidget = {'id':{
            'type':Entry,
            'typeData':StringVar(),
            'isID':True,
            'isReadOnly':True
        },
        'name':{
            'type':Entry,
            'typeData':StringVar(),
            'isID':True
        },
        'currentUsername':{
            'type':Entry,
            'typeData':StringVar(),
            'isID':True
        },
        'username':
        {
            'type':Entry,
            'typeData':StringVar()
        },
        'email':{
            'type':Entry,
            'typeData':StringVar(),
        },
        'role':{
            'type':Combobox,
            'typeData':StringVar(),
            'values':['Học viên - STUDENT','Giảng viên - LECTURER']
        }
        }

    def submitActionThread(self):
        values=self.getDataOfForm()
        # print(self.service.inssuanceNewAccount('student',values))


        
    