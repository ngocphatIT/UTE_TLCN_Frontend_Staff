class LecturerModel:
    def __init__(self,lid=None,account=None, name=None, personID=None, typePersonID=None,datetimeInit=None, isDeleted=False):
        self.stid=lid
        self.name=name
        self.account=account
        self.personID=personID
        self.typePersonID=typePersonID
        self.datetimeInit=datetimeInit
        self.isDeleted=isDeleted
    def getColumnID(self):
        return ['lid', 'name','account','personID','typePersonID','datetimeInit']
    def getColumnShow(self):
        return ['Mã giảng viên','Tên','Tài khoản đăng nhập','Mã số định danh','Loại định danh','Ngày tạo']
    def getColumnShowByID(self,id):
        return self.getColumnShow()[self.getColumnID().index(id)]
    def convertToJson(self):
        return {'lid':self.lid,'name':self.name,'account':self.account,'personID':self.personalID,'typePersonID':self.typePersonalID,'datetimeInit':self.datetimeInit}