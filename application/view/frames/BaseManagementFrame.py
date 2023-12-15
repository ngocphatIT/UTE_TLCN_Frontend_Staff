from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from ...myLib.DataGridView import DataGridView
from ...myLib.myTkinterThreading import MyTkinterThreading
from threading import Thread
import datetime
import time
_titleFont=('Arial',14,'bold')
_buttonFont=('Arial',14)
_statusActionFont=('Arial',12)
_myThread=MyTkinterThreading

class BaseManagementFrame(Frame):
    def __init__(self,master,mainScreen,model,service,addDataDialog,editDataDialog,title,size=(1440,720)):
        Frame.__init__(self)
        if mainScreen is None:
            mainScreen = master.master
        self.master = master
        self.lblTitle=Label(self,text=title,font=_titleFont)
        self.ctrlFrame=Frame(self)
        self.model=model()
        self.myTable=DataGridView(self,IDColumns=['STT']+self.model.getColumnID(),showColumns=['STT']+self.model.getColumnShow(), show="headings",height=30)
    
        self.addDataDialog=addDataDialog
        self.editDataDialog=editDataDialog
        self.service=service()
        self.mainScreen=mainScreen
        if size is not None:
            self.mainScreen.changeSize(size)
    def startWaiting(self,message):
        self.threadWaiting=Thread(target=self.waiting,args=(message,))
        self.threadWaiting.start()
    def getIsWaiting(self):
        return self.isWaiting
    def setIsWaiting(self,value):
        self.isWaiting = value
    def waiting(self,message):
        current_datetime = datetime.datetime.now()
        self.isWaiting = True
        wait=True
        while wait:
            self.lblStatusAction.config(text=message+'.'*((datetime.datetime.now()-current_datetime).seconds%3+1))
            time.sleep(0.25)
            wait=self.getIsWaiting()
        self.lblStatusAction.config(text="")
    def getDataFromBackend(self):
        try:
            response=self.handleErrorRepsonse(self.service.getByFilter())
            if response[0]:
                self.myTable.addRows(response[1]['message'])
        except Exception as e:
            print(e)
            # print(response)
        self.isWaiting=False
    def addModel(self,model):
        self.myTable.addRow(model)
    def btnAddAction(self):
        # self.mainScreen.hidden()
        self.addDataDialog(self.mainScreen,self).run()
    def handleErrorRepsonse(self,response):
        if response['status_code']==403:
            messagebox.showerror("Lỗi xác thực","Xác thưc hết hạn! Vui lòng đăng nhập lại")
            self.master.goBackLogin()
            return False,''
        return True,response
    def error403(self):
        messagebox.showerror("Lỗi xác thực","Xác thực hết hạn! Vui lòng đăng nhập lại")
        self.master.goToLogin()
    def btnEditAction(self):
        selected=self.myTable.getSelectedItem(mode='MAP')
        self.editDataDialog(self.mainScreen,self,selected).run()
    def btnDeleteAction(self):
        selected=self.myTable.getSelectedItem(mode='MAP')
        name=selected[self.model.getColumnID()[1]]
        res=messagebox.askquestion('Xóa', f'Bạn có chắc chắn muốn xóa "{name}" không?')
        if res == 'yes' :
            if self.service.delete(selected[self.model.getColumnID()[0]])[0]=='Deleted':
                self.refreshData()
                messagebox.showinfo('Thành công',"Xóa thành công!")
        else:
            pass
    def searchActionThread(self):
        try:
            response=self.handleErrorRepsonse(self.service.getByFilter({self.myTable.convertShowColumnToIDColumn(self.typeSearch.get()):self.entrySearch.get()}))
            if response[0]:
                self.myTable.removeAllData()
                self.myTable.addRows(response[1]['message'])
        except Exception as e:
            print(e)
            print(response)
    def btnSearchAction(self):
        _myThread().newThread(function=self.searchActionThread,message='Đang tìm kiếm',labelObject=self.lblStatusAction,functionCheckStatus=self.getIsWaiting,functionSetCheck=self.setIsWaiting)
    def refreshData(self):
        self.myTable.removeAllData()

        _myThread().newThread(function=self.getDataFromBackend,labelObject=self.lblStatusAction,functionCheckStatus=self.getIsWaiting,functionSetCheck=self.setIsWaiting)

    def btnRefreshAction(self):
        self.refreshData()
    def setupTitle(self,title="Chào mừng"):
        self.lblTitle.config(text=title)
    def setupCtrlDefault(self,modelName=""):
        self.btnAdd=Button(self.ctrlFrame,text=f"Thêm {modelName}",command=self.btnAddAction)
        self.btnEdit=Button(self.ctrlFrame,text=f'Chỉnh sửa {modelName}',command=self.btnEditAction)
        self.btnRemove=Button(self.ctrlFrame,text=f'Xóa {modelName}',command=self.btnDeleteAction)
        self.btnRefreshData=Button(self.ctrlFrame,text=f'Tải dữ liệu mẫu',command=self.btnRefreshAction)
        self.lblSearch=Label(self.ctrlFrame,text="Tìm kiếm")
        self.typeSearch=Combobox(self.ctrlFrame,values=self.model.getColumnShow(),state='readonly')
        self.typeSearch.current(0)
        self.searchValue=StringVar()
        self.entrySearch=Entry(self.ctrlFrame,textvariable=self.searchValue)
        self.btnSearch=Button(self.ctrlFrame,text="Tìm kiếm",command=self.btnSearchAction)
        self.lblStatusAction=Label(self,font=_statusActionFont)
    def packCtrlDefault(self):
        self.btnAdd.grid(row=0,column=0,padx=10)
        self.btnEdit.grid(row=0,column=1,padx=10)
        self.btnRemove.grid(row=0,column=2,padx=10)
        self.btnRefreshData.grid(row=0,column=3,padx=10)
        self.lblSearch.grid(row=1,column=0,padx=10)
        self.typeSearch.grid(row=1,column=1,padx=10)
        self.entrySearch.grid(row=1,column=2,padx=10)
        self.btnSearch.grid(row=1,column=3,padx=10)
    def packFrame(self):
        self.lblTitle.pack()
        self.lblStatusAction.pack()
        self.ctrlFrame.pack(pady=10)
        # self.runDemo()
        # self.getDataFromBackend()
        self.packData()
        self.pack()
    def runDemo(self):
        self.myTable=DataGridView(self,IDColumns=["ID", "Name", "Email", "Major"],showColumns=["ID DEMO", "Name DEMO", "Email DEMO", "Major DEMO"], show="headings")
        self.myTable.addRows([
            {"ID": 1, "Name": "John Doe", "Email": "johndoe@example.com", "Major": "Computer Science"},
            {"ID": 2, "Name": "Jane Doe", "Email": "janedoe@example.com", "Major": "Mathematics"},
            {"ID": 3, "Name": "Peter Jones", "Email": "peterjones@example.com", "Major": "Physics"},
            {"ID": 4, "Name": "Mary Smith", "Email": "marysmith@example.com", "Major": "Biology"},
            {"ID": 5, "Name": "David Williams", "Email": "davidwilliams@example.com", "Major": "Chemistry"},
        ])

    def _item_click(self, event):
        assert event.widget == self
        x, y = event.x, event.y
        element = self.identify("element", x, y)
        if element == "text":
            iid = self.identify_row(y)
            self._clicked(iid)

    def packData(self,filter=None):
        if filter is not None:
            self.myTable.pack(filter)
        self.myTable.pack()