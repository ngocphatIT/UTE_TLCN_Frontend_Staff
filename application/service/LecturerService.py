
from ..service.BaseModelService import BaseModelService
class LecturerService(BaseModelService):
    def __init__(self):
        BaseModelService.__init__(self,'lecturer')
    def getAll(self):
        return self.api.sendRequest(f'/api/{self.url}/getAllProfile',method='GET')[0]['data']
    def getByFilter(self, filter={}):
        return super().getByFilter(filter)
