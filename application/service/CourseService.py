
from ..service.BaseModelService import BaseModelService
class CourseService(BaseModelService):
    def __init__(self):
        BaseModelService.__init__(self,'course')
    def getAll(self):
        return self.api.sendRequest(f'/api/{self.url}/getAllInfo',method='GET')
