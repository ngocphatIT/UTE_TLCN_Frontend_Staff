from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from ...dialog.AddDataDialog.BaseAddDialog import BaseAddDialog
from ....model.CourseCategoryModel import CourseCategoryModel
from ....service.CourseCategoryService import CourseCategoryService

_service = CourseCategoryService()
class AddCourseCategoryDialog(BaseAddDialog):
    def __init__(self,tkMaster,master,title='Thêm loại khóa học',data=None,model=CourseCategoryModel,service=CourseCategoryService):
        super().__init__(tkMaster,master,title,data,model,service)
        self.dictInfoWidget = {'cid':{
            'type':Entry,
            'typeData':StringVar(),

        },
        'nameCategory':{
            'type':Entry,
            'typeData':StringVar(),
        },
        'description':{
            'type':Entry,
            'typeData':StringVar(),
        }}
    
