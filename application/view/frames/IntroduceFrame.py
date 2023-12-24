from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from ...service.SQLLiteService import SessionDataService
from ...service.StaffService import StaffService
from ...myLib.myJWT import decode

_titleFont = ("Arial", 15, "bold")
_textFont = ("Arial", 13)
_session=SessionDataService
_service = StaffService

class IntroduceFrame(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        Label(self,text="TIỂU LUẬN CHUYÊN NGÀNH HK1/23-24",font=_titleFont).pack()
        Label(self,text="Chuyên ngành: Hệ thống thông tin",font=_textFont).pack()
        Label(self,text="Sinh viên thực hiện: Nguyễn Ngọc Phát - Lý Hồng Phát",font=_textFont).pack()
        Label(self,text="Giảng viên hướng dẫn: Võ Xuân Thể",font=_textFont).pack()
        Label(self).pack()
        Label(self,text="Sản phẩm windows app dành cho phân hệ Nhân viên ",font=_textFont).pack()
        Label(self,text="[Sản phẩm phục vụ cho mục đích học tập]",font=_textFont).pack()
    def clear(self):
        for widget in self.winfo_children():
            widget.destroy()
    def packFrame(self):
        self.pack()
        
            


