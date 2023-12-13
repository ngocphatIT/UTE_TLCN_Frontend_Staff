class CourseCategoryModel:
    def __init__(self,cid=None,name=None,isDeleted=False,description=None):
        self.cid=cid
        self.name=name
        self.isDeleted=isDeleted
        self.description=description
    def getColumnID(self):
        return ['cid', 'nameCategory','description', 'isDeleted']
    def getColumnShow(self):
        return ['Mã loại khóa học', 'Tên','Mô tả','Đã xóa']
    def getColumnShowByID(self,id):
        return self.getColumnShow()[self.getColumnID().index(id)]
    def convertToJson(self):
        return {'cid':self.cid,'nameCategory':self.name,'description':self.description,'isDeleted':self.isDeleted}