from tkinter import *
from tkinter import messagebox
from ..frames.BaseManagementFrame import BaseManagementFrame
from ...myLib.DataGridView import DataGridView
from ...model.CourseModel import CourseModel
from ...view.dialog.AddDataDialog.AddCourseDialog import AddCourseDialog
from ...view.dialog.EditDataDialog.EditCourseDialog import EditCourseDialog
from ...service.CourseService import CourseService
class CourseManagementFrame(BaseManagementFrame):
    def __init__(self,master,mainScreen=None):
        super().__init__(master=master,mainScreen=mainScreen,model=CourseModel,service=CourseService,addDataDialog=AddCourseDialog,editDataDialog=EditCourseDialog,title='Quản lý khóa học')
        # self.setupTitle()
        self.setupCtrlDefault()
        self.packCtrlDefault()