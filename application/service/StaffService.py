
from ..service.BaseModelService import BaseModelService
class StaffService(BaseModelService):
    def __init__(self):
        BaseModelService.__init__(self,'staff')
    def getProfileByAccountID(self,aid):
        return self.api.sendRequest(f'/api/{self.url}/getProfileByAccountID/{aid}',method='GET')
    def update(self,id,model):
        return self.api.sendRequest(f'/api/{self.url}/update/{id}',method='PUT',data=model)
    def getByFilter(self, filter={}):
        return super().getByFilter(filter)
