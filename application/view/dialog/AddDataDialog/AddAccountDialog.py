from tkinter import *
from tkinter.ttk import *

from ...dialog.AddDataDialog.BaseAddDialog import BaseAddDialog
from ....model.AccountModel import AccountModel

from ....service.AccountService import AccountService
from ....service.RoleService import RoleService
from datetime import date

today = str(date.today())
_roleService = RoleService()
class AddAccountDialog(BaseAddDialog):
    def __init__(self,tkMaster,master,title='Cấp tài khoản',data=None,model=AccountModel,service=AccountService,role='STUDENT'):
        super().__init__(tkMaster,master,title,data,model,service)
        roles=_roleService.getAll()['message']

        roleValues=[]
        for i in roles:
            if not i['isDeleted'] and i['rolename'].upper()!='ADMIN':
                roleValues.append(f"{i['rolename']} - {i['rid']}")
        self.dictInfoWidget = {'uuid':{
            'type':Entry,
            'typeData':StringVar(),
        },
        'username':{
            'type':Entry,
            'typeData':StringVar(),
        },
        'email':{
            'type':Entry,
            'typeData':StringVar(),
        },
        'datetimeInit':{
            'type':Entry,
            'typeData':StringVar()
        },
        'role':{
            'type':Combobox,
            'typeData':StringVar(),
            'isReadOnly':True,
            'values':roleValues
        }}
        self.role=role
    def submitActionThread(self):
        values=self.getDataOfForm()

    