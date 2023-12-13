class AccountModel:
    def __init__(self,uuid=None, username=None,passwordHash=None, datetimeInit=None,isDeleted=False,role=None):
        self.uuid = uuid
        self.username = username
        self.passwordHash = passwordHash
        self.datetimeInit = datetimeInit
        self.isDeleted = isDeleted
        self.role=role
    def getColumnID(self):
        return ['uuid','username','email','role','datetimeInit','isDeleted']
    def getColumnShow(self):
        return ['Mã tài khoản','Tên đăng nhập','Email','Quyền tài khoản','Ngày tạo','Đã xóa']
    def getColumnShowByID(self,id):
        return self.getColumnShow()[self.getColumnID().index(id)]
    def convertToJson(self):
        return {'uuid':self.uuid,'username':self.username,'passwordHash':self.passwordHash,'datetimeInit':self.datetimeInit,'isDeleted':self.isDeleted,'role':self.role}