
from ..service.BaseModelService import BaseModelService
class CourseService(BaseModelService):
    def __init__(self):
        BaseModelService.__init__(self,'course')
    def getByFilter(self, filter={}):
        return super().getByFilter(filter)