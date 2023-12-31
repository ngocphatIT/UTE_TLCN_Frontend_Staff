import datetime
class ClassModel:
    def __init__(self,cid=None, className=None, description=None, datetimeStart=None,datetimeEnd=None,course=None,isDeleted=False):
        self.cid=cid
        self.className=className
        self.description=description
        self.datetimeStart=datetimeStart
        self.datetimeEnd=datetimeEnd
        self.course=course
        self.isDeleted=isDeleted
    def getColumnID(self):
        return ['cid','className','description','dateStart','dateEnd','course']
    def getColumnShow(self):
        return ['Mã lớp học','Tên','Mô tả','Ngày bắt đầu','Ngày kết thúc','Khóa học']
    def getColumnShowByID(self,id):
        return self.getColumnShow()[self.getColumnID().index(id)]
    def convertToJson(self):
        return {'cid': self.cid,'className': self.className,'description': self.description,'course':self.course,'datetimeStart':datetime.fromisoformat(self.datetimeStart.isoformat()),'datetimeEnd':datetime.fromisoformat(self.datetimeEnd.isoformat())}