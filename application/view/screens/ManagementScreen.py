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
from ...service.AccountService import AccountService
_accountService=AccountService
class ManagementScreen(Frame):
    def __init__(self,master):
        Frame.__init__(self)
        self.currentFrame = None
        self.lastFrame = None
        self.master = master
        self.master.title("Student Management System")
        menubar=Menu(self)
        # Create the Teacher Management menu
        myProfile = Menu(menubar, tearoff=0)
        myProfile.add_command(label="My profile")
        myProfile.add_command(label="Đăng xuất",command=self.logout )

        # myProfile.add_command(label="Delete Teacher")
        menubar.add_cascade(label="My Profile", menu=myProfile)

        groupClass = Menu(menubar, tearoff=0)
        groupClass.add_command(label="Course Category Management",command=lambda: self.showFrame("Course Category Management"))
        groupClass.add_command(label="Course Management",command=lambda: self.showFrame("Course Management"))
        groupClass.add_command(label="Class Management",command=lambda: self.showFrame("Class Management"))
        menubar.add_cascade(label="Group Class Management", menu=groupClass)

        # Create the Student Management menu
        groupUser = Menu(menubar, tearoff=0)
        groupUser.add_command(label="Student Management",command=lambda: self.showFrame("Student Management"))
        groupUser.add_command(label="Lecturer Management",command=lambda: self.showFrame("Lecturer Management"))
        groupUser.add_command(label="Account Management",command=lambda: self.showFrame("Account Management"))
        menubar.add_cascade(label="User Management", menu=groupUser)
        self.master.config(menu=menubar)
        # self.showFrame()
    def getFrame(self,frame):
        dictFrame={
            # 'Student Management':StudentManagementFrame
            'Course Category Management':CourseCategoryManagementFrame,
            'Course Management':CourseManagementFrame,
            'Class Management':ClassManagementFrame,
            'Student Management':StudentManagementFrame,
            'Lecturer Management':LecturerManagementFrame,
            'Account Management':AccountManagementFrame,
            'View Participants':ViewParticipantsFrame
            
            
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

        # # Initially, display the Class Management frame
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
        # notebook.add(student_tab, text="Student Management")
        # notebook.add(lecturer_tab, text="Lecturer Management")
        # notebook.add(account_tab, text="Account Management")
        # notebook.pack(fill="both", expand=True)
        # student_tab.packData({'fill':"both", 'expand':True})