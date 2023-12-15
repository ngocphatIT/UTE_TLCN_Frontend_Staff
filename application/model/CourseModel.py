class CourseModel:
    def __init__(self,cid=None,courseName=None, description=None, category=None, isDeleted=False):
        self.cid=cid
        self.courseName=courseName
        self.description=description
        self.category=category
        self.isDeleted=isDeleted
    def getColumnID(self):
        return ['cid', 'courseName', 'description', 'category']
    def getColumnShow(self):
        return ['Mã khóa học','Tên khóa học','Mô tả','Loại khóa học']
    def getColumnShowByID(self,id):
        return self.getColumnShow()[self.getColumnID().index(id)]
    def convertToJson(self):
        return {'cid':self.cid,'courseName':self.courseName,'category':self.category,'description':self.description}