
from ..service.BaseModelService import BaseModelService
class ClassService(BaseModelService):
    def __init__(self):
        BaseModelService.__init__(self,'class')
    def getAll(self):
        return self.api.sendRequest(f'/api/{self.url}/getAllInfoAllClass',method='GET')
