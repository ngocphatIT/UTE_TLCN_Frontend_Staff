class ParticipantsClassModel:
    def __init__(self,id=None,name=None,accountID=None,role=None):
        self.id=id
        self.name=name
        self.accountID=accountID
        self.role=role
    def getColumnID(self):
        return ['id','name','role','accountID']
    def getColumnShow(self):
        return ['Mã học viên/giảng viên','Tên','Đối tượng','accountID']
    def getColumnShowByID(self,id):
        return self.getColumnShow()[self.getColumnID().index(id)]
    def convertToJson(self):
        return {'id':self.id,'name':self.name,'accountID':self.accountID,'role':self.role}