from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from ....myLib.myTkinterThreading import MyTkinterThreading
_fontLbl=('Arial',13)
_fontTitle=('Arial',15,'bold')
_myThread=MyTkinterThreading
_statusActionFont=('Arial',12)
class BaseAddDialog(Toplevel):
    def __init__(self,tkMaster,master,title='Xin chào',data=None,model=None,service=None):
        Toplevel.__init__(self)
        self.tkMaster=tkMaster
        self.title=title
        self.master=master
        self.protocol('WM_DELETE_WINDOW', self.doSomething)
        self.model=model
        self.service=service()
        self.dictInfoWidget={}
        self.widgets={}
        self.data=data
    # def setupInfoWidget(self):
    #     dictTypeWidget={
    #         'entry':Entry,
    #         'combobox':Combobox,
    #     }
    #     for i in self.dictInfoWidget.keys():
    #         temp={}
    #         value=self.dictInfoWidget[i]
    #         # if value['typeData']=='string':
    #         temp['value']=StringVar()
    #         temp['entry']=dictTypeWidget[value['type']](self)
    #         temp['title']=self.model.getColumnShowByID(i)
    #         self.widgets[i]=temp
    #         print(temp)
    def getIsWaiting(self):
        return self.isWaiting
    def setIsWaiting(self,value):
        self.isWaiting = value
    def setupWidget(self):
        defaultValue={'isOptional':False, 'isID':False,'isReadOnly':False,'width':50,'padx':5,'pady':5}
        Label(self,text=self.title,font=_fontTitle).grid(columnspan=2)
        self.lblStatusAction=Label(self,font=_statusActionFont)
        self.lblStatusAction.grid(columnspan=2)
        row=2
        for i in self.dictInfoWidget.keys():
            column=0
            w=self.dictInfoWidget[i]
            for la in defaultValue.keys():
                if la not in w:
                    w[la]=defaultValue[la]  
            title=self.model().getColumnShowByID(i)
            if w['isOptional']:
                title=title+" (optional)"
            else:
                title=title+" *"
            Label(self,text=title,font=_fontLbl).grid(row=row,column=column,sticky='e',padx=w['padx'],pady=w['pady'])
            column=column+1
            
            w['type']=w['type'](self,font=_fontLbl,width=50)
            w['type'].config(state='normal')
            w['type'].config(textvariable=w['typeData'])
            if 'values' in w:
                if type(w['type'])==Combobox:
                    w['type'].config(values=w['values'],width=w['width'])
                    if 'currentChoice' not in w:
                        w['currentChoice']=0
                    w['type'].current(w['currentChoice'])
                else:
                    w['typeData'].set(w['values'])
            if 'config' in w:
                w['type'].config(**w['config'])
            if w['isReadOnly']:
                w['type'].config(state='readonly')
            if w['isID']:
                w['type'].config(state='disabled')
            w['type'].grid(row=row,column=column,sticky='w',padx=w['padx'],pady=w['pady'])
            row+=1
        self.btnSubmit=Button(self,text='Submit',command=self.btnSubmitAction)
        self.btnSubmit.grid(row=row,column=1)
    def updateData(self,data=None):
        pass
    def getDataOfForm(self):
        temp={}
        for i in self.dictInfoWidget.keys():
            temp[i]=" ".join(self.dictInfoWidget[i]['type'].get().split())
            if type(self.dictInfoWidget[i]['typeData']) == BooleanVar:
                if temp[i]=='True':
                    temp[i]=True
                else:
                    temp[i]=False
        return temp
    def btnSubmitAction(self):
        _myThread().newThread(function=self.submitActionThread,message='Đang thực hiện',labelObject=self.lblStatusAction,functionCheckStatus=self.getIsWaiting,functionSetCheck=self.setIsWaiting)
    def submitActionThread(self):
        category=self.getDataOfForm()
        response=self.service.create(category)
        if response['status_code']==403:
            self.master.error403()
            return
        if response['status_code']==201:
            self.master.refreshData()
            messagebox.showinfo("Thành công","Thêm thành công!")
        else:
            messagebox.showerror("Lỗi","Định dạng dữ liệu không phù hợp")
        self.isWaiting=False
    def doSomething(self):
        self.destroy()
        self.tkMaster.comeback()
    def run(self):
        self.updateData(self.data) 
        self.setupWidget()

