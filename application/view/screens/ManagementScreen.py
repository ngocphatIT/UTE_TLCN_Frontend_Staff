from tkinter import *
from tkinter import messagebox
# from ..frames.StudentManagementFrame import StudentManagementFrame
from ..frames.CourseCategoryManagementFrame import CourseCategoryManagementFrame
from ..frames.CourseManagementFrame import CourseManagementFrame
from ..frames.ClassManagementFrame import ClassManagementFrame
from ..frames.StudentManagementFrame import StudentManagementFrame
from ..frames.LecturerManagementFrame import LecturerManagementFrame
from ..frames.AccountManagementFrame import AccountManagementFrame
from ..frames.ViewParticipantsFrame import ViewParticipantsFrame
from ..frames.MyProfileFrame import MyProfileFrame
from ...service.AccountService import AccountService
_accountService=AccountService
_fontMenuHeader=('Arial',12)
_fontMenuSub=('Arial',11)
class ManagementScreen(Frame):
    def __init__(self,master):
        Frame.__init__(self)
        self.currentFrame = None
        self.lastFrame = None
        self.master = master
        self.master.title("Management System")
        menubar=Menu(self)
        # Create the Teacher Management menu
        myProfile = Menu(menubar, tearoff=0)
        myProfile.add_command(label="Thông tin của tôi",font=_fontMenuSub,command=lambda: self.showFrame("Thông tin của tôi"))
        myProfile.add_command(label="Đổi mật khẩu",font=_fontMenuSub,command=self.changePassword)
        myProfile.add_command(label="Đăng xuất",font=_fontMenuSub,command=self.logout)

        # myProfile.add_command(label="Delete Teacher")
        menubar.add_cascade(label="Tôi",font=_fontMenuHeader, menu=myProfile)

        groupClass = Menu(menubar, tearoff=0)
        groupClass.add_command(label="Quản lý loại khóa học",font=_fontMenuSub,command=lambda: self.showFrame("Quản lý loại khóa học"))
        groupClass.add_command(label="Quản lý khóa học",font=_fontMenuSub,command=lambda: self.showFrame("Quản lý khóa học"))
        groupClass.add_command(label="Quản lý lớp học",font=_fontMenuSub,command=lambda: self.showFrame("Quản lý lớp học"))
        menubar.add_cascade(label="Nhóm lớp học",font=_fontMenuHeader,menu=groupClass)

        # Create the Quản lý học viên menu
        groupUser = Menu(menubar, tearoff=0)
        groupUser.add_command(label="Quản lý học viên",font=_fontMenuSub,command=lambda: self.showFrame("Quản lý học viên"))
        groupUser.add_command(label="Quản lý giảng viên",font=_fontMenuSub,command=lambda: self.showFrame("Quản lý giảng viên"))
        groupUser.add_command(label="Quản lý tài khoản",font=_fontMenuSub,command=lambda: self.showFrame("Quản lý tài khoản"))
        menubar.add_cascade(label="Nhóm người dùng",font=_fontMenuHeader, menu=groupUser)
        self.master.config(menu=menubar)
        # self.showFrame()
    def getFrame(self,frame):
        dictFrame={
            # 'Student Management':StudentManagementFrame
            'Quản lý loại khóa học':CourseCategoryManagementFrame,
            'Quản lý khóa học':CourseManagementFrame,
            'Quản lý lớp học':ClassManagementFrame,
            'Quản lý học viên':StudentManagementFrame,
            'Quản lý giảng viên':LecturerManagementFrame,
            'Quản lý tài khoản':AccountManagementFrame,
            'Quản lý thành viên lớp học':ViewParticipantsFrame,
            'Thông tin của tôi':MyProfileFrame
        }
        return dictFrame[frame](self)
    def showViewParticipants(self,classID,className):
        self.lastFrame=self.currentFrame
        self.currentFrame=ViewParticipantsFrame(master=self,classID=classID,className=className)
        if self.lastFrame is not None:
            self.lastFrame.pack_forget()
        self.currentFrame.packFrame()
        self.currentFrame.tkraise()
    def showFrame(self,name):
        self.lastFrame=self.currentFrame
        self.currentFrame=self.getFrame(name)
        if self.lastFrame is not None:
            self.lastFrame.pack_forget()
        self.currentFrame.packFrame()
        self.currentFrame.tkraise()
    def changePassword(self):
        self.master.goToChangePassword(isLogin=True)

        
    def logout(self):
        res=messagebox.askquestion('Xóa', f'Bạn có chắc chắn muốn đăng xuất không?')
        if res=='yes':
            response=_accountService().logout()
            if response['status_code']==201:
                self.master.goToLogin()
    def goBackLogin(self):
        return self.master.goToLogin()



        # Create the frames for each menu item
        
        # class_frame = Frame(self)
        # student_frame = Frame(self)
        # teacher_frame = Frame(self)

        # # Initially, display the Quản lý lớp học frame
        # class_frame.pack()
        

        # Bind the menu selection event to the menu_selected function
        # class_menu.bind("<Button-1>", menu_selected)
        # student_menu.bind("<Button-1>", menu_selected)
        # teacher_menu.bind("<Button-1>", menu_selected)
        
        # notebook = ttk.Notebook(self.master)
        # lecturer_tab = ttk.Frame(notebook)
        # account_tab = ttk.Frame(notebook)
        # student_tab = StudentManagementFrame(notebook)
        # student_tab.runDemo()
        # notebook.add(student_tab, text="Quản lý học viên")
        # notebook.add(lecturer_tab, text="Quản lý giảng viên")
        # notebook.add(account_tab, text="Quản lý tài khoản")
        # notebook.pack(fill="both", expand=True)
        # student_tab.packData({'fill':"both", 'expand':True})