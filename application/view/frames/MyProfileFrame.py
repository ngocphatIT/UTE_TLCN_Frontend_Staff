from tkinter import *
from tkinter.ttk import Combobox
from ...service.SQLLiteService import SessionDataService
from ...service.StaffService import StaffService
from ...myLib.myJWT import decode

_titleFont = ("Arial", 15, "bold")
_textFont = ("Arial", 13)
_session=SessionDataService
_service = StaffService

class MyProfileFrame(Frame):
    def __init__(self, master, mainScreen=None):
        Frame.__init__(self)
        self.master = master
        if mainScreen is None:
            mainScreen = master.master
        self.mainScreen = mainScreen
        self.dictValue = {
            'id':StringVar(),
            "name": StringVar(),
            "personID": StringVar(),
            "typePersonalID": StringVar(),
            "account": StringVar(),
        }
        self.dictInfoWidget={
            'id':{
                'title':"Mã nhân viên: ",
                'dataType':StringVar(),
                'type':Entry,
            },
            'name':{
                'title':"Tên nhân viên: ",
                'dataType':StringVar(),
                'type':Entry
            },
            'personID':
            {
                'title':'Mã số định danh: ',
                'dataType':StringVar(),
                'type':Entry
            },
            'typePersonID':
            {
                'title':'Loại định danh: ',
                'dataType':StringVar(),
                'type':Entry
            },
            'account':
            {
                'title':'Tài khoản đăng nhập: ',
                'dataType':StringVar(),
                'type':Entry
            }
        }
        self.mainScreen.changeSize((500,300))
        self.dictWidget={}
        
    def getProfile(self):
        response=_service().getProfileByAccountID(decode(_session().getAuthorization(),'')['payload']['sub'])
        for i in self.dictInfoWidget:
            isPass=False
            if response is not None:
                if response['status_code']==200:
                    isPass=True
                    self.dictInfoWidget[i]['dataType'].set(response['message'][i])
            if not isPass:
                self.dictInfoWidget[i]['dataType'].set('Đang cập nhật...')
    def setup(self):
        row=0
        self.lblTitle = Label(self, text="Thông tin cá nhân", font=_titleFont)
        self.lblTitle.grid(columnspan=4)
        row+=1
        for i in self.dictInfoWidget.keys():
            lbl=Label(self,text=self.dictInfoWidget[i]['title'],font=_textFont)
            lbl.grid(column=0, columnspan=2, row=row,sticky='e')
            type=self.dictInfoWidget[i]['type'](self,textvariable=self.dictInfoWidget[i]['dataType'],font=_textFont)
            if 'width' in self.dictInfoWidget[i]:
                type.config(width=self.dictInfoWidget[i]['width'])
            type.grid(column=2, columnspan=2, row=row,pady=5,ipadx=50,sticky='w')
            type.config(state='readonly')
            temp={'label':lbl,'type':type}
            self.dictWidget[i]=temp
            row+=1
        # self.btnEdit=Button(self,text='Chỉnh sửa',font=_textFont)
        # self.btnEdit.grid(row=row,column=2,pady=20)
        # # self.btnChangePassword=Button(self,text='Đổi mật khẩu')
        # # self.btnChangPassword(row=row,column=2)
        # self.btnCancel=Button(self,text='Hủy',font=_textFont)
        # self.btnCancel.grid(row=row,column=3,sticky='w')
        

    def packFrame(self):
        # self.lblTitle.pack()
        # self.lblStatusAction.pack()
        # self.ctrlFrame.pack(pady=10)
        # # self.runDemo()
        # # self.getDataFromBackend()
        # self.packData()
        self.getProfile()
        self.setup()
        self.pack()
            


