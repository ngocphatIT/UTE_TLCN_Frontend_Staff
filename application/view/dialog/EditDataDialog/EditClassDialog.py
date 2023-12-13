from ...dialog.AddDataDialog.AddClassDialog import AddClassDialog
from ....service.ClassService import ClassService
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
_service=ClassService()
class EditClassDialog(AddClassDialog):
    def __init__(self,tkMaster,master,data,title='Xin chào'):
        super().__init__(tkMaster,master,title,data)
        self.data=data
        self.dictInfoWidget['cid']['isID']=True
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
                

        
        