from tkinter import *
from tkinter.ttk import *
from ...dialog.AddDataDialog.BaseAddDialog import BaseAddDialog
from ....model.CourseModel import CourseModel
from ....service.CourseService import CourseService
from ....service.CourseCategoryService import CourseCategoryService
class AddCourseDialog(BaseAddDialog):
    def __init__(self,tkMaster,master,title='Xin chào',data=None,model=CourseModel,service=CourseService):
        super().__init__(tkMaster,master,title,data,model,service)
        cat=CourseCategoryService().getAll()['message']
        catValue=[]
        for i in cat:
            if 'isDeleted' not in i:
                i['isDeleted']=False
            if not i['isDeleted']:
                catValue.append(i['nameCategory'])
        self.dictInfoWidget = {'cid':{
            'type':Entry,
            'typeData':StringVar()
        },
        'courseName':{
            'type':Entry,
            'typeData':StringVar(),
        },
        'category':
        {
            'type':Combobox,
            'typeData':StringVar(),
            'values':catValue,
            'currentChoice':0,
            'isReadOnly':True,
            'width':20
        },
        'description':{
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
        }}

    