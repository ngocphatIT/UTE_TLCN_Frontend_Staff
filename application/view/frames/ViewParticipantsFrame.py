from ..frames.BaseManagementFrame import BaseManagementFrame
from tkinter import *
from tkinter import messagebox
from ...service.ClassService import ClassService
from ...model.ParticipantsClassModel import ParticipantsClassModel
from ..dialog.AddDataDialog.AddParticipantsDialog import AddParticipantsDialog
import time
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
        self.isWaiting=False
    def deletedActionThread(self):
        try:
            selected=self.myTable.getSelectedItem(mode='MAP')
            res=messagebox.askquestion('Xóa', f'''Bạn có chắc chắn muốn xóa {selected['role']} "{selected['name']}" không?''')
            del selected['accountID']
            del selected['name']
            del selected['STT']
            if res == 'yes' :
                response=self.service.deleteParticipants(self.classID,selected)
                if response['status_code']==201:
                    self.refreshData()
                    messagebox.showinfo('Thành công',"Xóa thành công!")
                else:
                    messagebox.showinfo('Thất bại',response['message'])
            else:
                pass
        except:
            messagebox.showerror("Xóa","Chưa chọn đối tượng!")
        self.isWaiting = False
    def searchActionThread(self):
        self.refreshData(isClearSearchValue=False)
        start_time = time.time()
        while self.myTable.isEmpty():
            if time.time()-start_time>=5:
                break
        if not self.myTable.search(self.typeSearch.get(),self.entrySearch.get()):
            messagebox.showinfo('Không tìm thấy',f'Không tìm thấy!')

