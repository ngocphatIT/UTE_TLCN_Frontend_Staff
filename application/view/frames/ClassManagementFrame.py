from ..frames.BaseManagementFrame import BaseManagementFrame
from tkinter import *
from ...service.ClassService import ClassService
from ...model.ClassModel import ClassModel
from ..dialog.AddDataDialog.AddClassDialog import AddClassDialog
from ..dialog.EditDataDialog.EditClassDialog import EditClassDialog
# from application.view.dialog.ViewDialog.ViewClassParticipantsDialog import ViewParticipantsDialog
# _viewParticipants=ViewParticipantsDialog
class ClassManagementFrame(BaseManagementFrame):
  def __init__(self,master,mainScreen=None):
    super().__init__(master=master,mainScreen=mainScreen,model=ClassModel,service=ClassService,addDataDialog=AddClassDialog,editDataDialog=EditClassDialog,title='Quản lý thông tin lớp học')
    # self.setupTitle()
    self.setupCtrlDefault()
    self.packCtrlDefault()
  def setupCtrlDefault(self, modelName=""):
    super().setupCtrlDefault(modelName)
    self.btnViewPartipants=Button(self.ctrlFrame,text="Xem thành viên",command=self.viewParticipants)
  def viewParticipants(self):
    selected=self.myTable.getSelectedItem(mode='MAP')
    if 'cid' in selected:
      self.master.showViewParticipants(classID=selected['cid'],className=selected['className'])
  def packCtrlDefault(self):
      super().packCtrlDefault()
      self.btnViewPartipants.grid(row=2,column=0)