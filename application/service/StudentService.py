
from ..service.BaseModelService import BaseModelService
class StudentService(BaseModelService):
    def __init__(self):
        BaseModelService.__init__(self,'student')
    def getAll(self):
        return self.api.sendRequest(f'/api/{self.url}/getAllProfile',method='GET')
    def getByFilter(self, filter={}):
        return super().getByFilter(filter)
