from ..frames.BaseManagementFrame import BaseManagementFrame
from tkinter import *
from tkinter import messagebox
from ...myLib.DataGridView import DataGridView
from ...service.CourseCategoryService import CourseCategoryService
from ...model.CourseCategoryModel import CourseCategoryModel
from ..dialog.AddDataDialog.AddCourseCategoryDialog import AddCourseCategoryDialog
from ..dialog.EditDataDialog.EditCourseCategoryDialog import EditCourseCatoryDialog
class CourseCategoryManagementFrame(BaseManagementFrame):
      def __init__(self,master):
        super().__init__(master=master,mainScreen=master.master,model=CourseCategoryModel,service=CourseCategoryService,addDataDialog=AddCourseCategoryDialog,editDataDialog=EditCourseCatoryDialog,title='Quản lý loại khóa học')