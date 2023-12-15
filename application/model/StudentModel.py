class StudentModel:
    def __init__(self,stid=None,account=None, name=None, personID=None, typePersonID=None,datetimeInit=None, isDeleted=False):
        self.stid=stid
        self.name=name
        self.account=account
        self.personID=personID
        self.typePersonID=typePersonID
        self.datetimeInit=datetimeInit
        self.isDeleted=isDeleted
    def getColumnID(self):
        return ['stid', 'name','account','personID','typePersonID','datetimeInit']
    def getColumnShow(self):
        return ['Mã học viên','Tên','Tài khoản đăng nhập','Mã số định danh','Loại định danh','Ngày tạo']
    def getColumnShowByID(self,id):
        return self.getColumnShow()[self.getColumnID().index(id)]
    def convertToJson(self):
        return {'stid':self.stid,'name':self.name,'account':self.account,'personID':self.personalID,'typePersonID':self.typePersonalID,'datetimeInit':self.datetimeInit}