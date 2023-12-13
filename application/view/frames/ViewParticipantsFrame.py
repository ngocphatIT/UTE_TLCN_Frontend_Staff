from ..frames.BaseManagementFrame import BaseManagementFrame
from tkinter import *
from tkinter import messagebox
from ...service.ClassService import ClassService
from ...model.ParticipantsClassModel import ParticipantsClassModel
from ..dialog.AddDataDialog.AddParticipantsDialog import AddParticipantsDialog
from ..dialog.EditDataDialog.EditAccountDialog import EditAccountDialog
class ViewParticipantsFrame(BaseManagementFrame):
    def __init__(self,master,mainScreen=None,classID='',className=''):
        self.classID=classID
        self.className=className
        super().__init__(master=master,mainScreen=mainScreen,model=ParticipantsClassModel,service=ClassService,addDataDialog=AddParticipantsDialog,editDataDialog=AddParticipantsDialog,title='Thành viên lớp học '+className)
        # self.setupTitle()
        self.setupCtrlDefault()
        self.packCtrlDefault()
        self.btnEdit.config(state='disabled')
        self.getDataFromBackend()
    def btnAddAction(self):
        # self.mainScreen.hidden()
        self.addDataDialog(self.mainScreen,self,classID=self.classID).run()
    def getDataFromBackend(self):
        try:
            response=self.handleErrorRepsonse(self.service.getAllParticipantsByClassID(self.classID))
            if response[0]:
                self.myTable.addRows(response[1]['message'])
        except Exception as e:
            print(e)
    def btnDeleteAction(self):
        selected=self.myTable.getSelectedItem(mode='MAP')
        res=messagebox.askquestion('Xóa', f'''Bạn có chắc chắn muốn xóa {selected['role']} "{selected['name']}" không?''')
        del selected['accountID']
        del selected['name']
        del selected['STT']
        if res == 'yes' :
            print(selected)
            response=self.service.deleteParticipants(self.classID,selected)
            if response['status_code']==201:
                self.refreshData()
                messagebox.showinfo('Thành công',"Xóa thành công!")
            else:
                messagebox.showinfo('Thất bại',response['message'])
        else:
            pass
    def btnSearchAction(self):
        self.refreshData()
        self.myTable.search(self.typeSearch.get(),self.entrySearch.get())