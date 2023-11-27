from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from ...dialog.AddDataDialog.BaseAddDialog import BaseAddDialog
from ....model.CourseCategoryModel import CourseCategoryModel
from ....service.CourseCategoryService import CourseCategoryService

_service = CourseCategoryService()
class AddCourseCategoryDialog(BaseAddDialog):
    def __init__(self,tkMaster,master,title='Xin chào',data=None,model=CourseCategoryModel,service=CourseCategoryService):
        super().__init__(tkMaster,master,title,data,model,service)
        self.dictInfoWidget = {'cid':{
            'type':Entry,
            'typeData':StringVar(),
            'isID':True,
        },
        'name':{
            'type':Entry,
            'typeData':StringVar(),
        },
        'isDeleted':{
            'type':Combobox,
            'typeData':BooleanVar(),
            'values':[False,True],
            'currentChoice':0,
            'isReadOnly':True,
            'width':10
        },
        'description':{
            'type':Entry,
            'typeData':StringVar(),
        }}
    
