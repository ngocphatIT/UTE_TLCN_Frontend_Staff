
from ..service.BaseModelService import BaseModelService
class AccountService(BaseModelService):
    def __init__(self):
        BaseModelService.__init__(self,'account')
    # def getAll(self):
    #     return self.api.sendRequest(f'/api/{self.url}/getAllInfoAllClass',method='GET')
    def inssuanceNewAccount(self,data):
        return self.api.sendRequest(f'/api/account/issuanceAccount',method='POST',data=data)
    def getByFilter(self, filter={}):
        return super().getByFilter(filter)
    def deleteRole(self,uuid,role):
        return self.api.sendRequest(f'/api/account/deleteRole/{uuid}/{role}',method='DELETE')