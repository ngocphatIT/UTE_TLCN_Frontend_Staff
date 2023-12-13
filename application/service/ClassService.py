
from ..service.BaseModelService import BaseModelService
class ClassService(BaseModelService):
    def __init__(self):
        BaseModelService.__init__(self,'class')
    def getByFilter(self, filter={}):
        return super().getByFilter(filter)
    def getAllParticipantsByClassID(self,id):
        return self.api.sendRequest(f'/api/{self.url}/getAllParticipantsByClassId/{id}',method='GET')
    def addParticipants(self,id,data):
        return self.api.sendRequest(f'/api/{self.url}/addParticipants/{id}',method='PUT',data=data)
    def deleteParticipants(self,id,data):
        return self.api.sendRequest(f'/api/{self.url}/deleteParticipants/{id}',method='PUT',data=data)
        
