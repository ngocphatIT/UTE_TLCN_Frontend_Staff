class IssuanceNewAccountModel:
    def __init__(self,id=None,name=None,currentUsername=None, username=None,type=None,email=None,role=None):
        self.id = id
        self.username = username
        self.email=email
        self.type=type
        self.role=role
        self.name=name
        self.currentUsername=currentUsername
    def getColumnID(self):
        return ['id','name','currentUsername','username','email','role']
    def getColumnShow(self):
        return ['Mã người dùng','Tên','Tên đăng nhập hiện tại','Tên đăng nhập','Email','Quyền tài khoản']
    def getColumnShowByID(self,id):
        return self.getColumnShow()[self.getColumnID().index(id)]
    def convertToJson(self):
        return {'id':self.aid,'currentUsername':self.currentUsername,'name':self.name,'username':self.username,'email':self.email,'role':self.role}