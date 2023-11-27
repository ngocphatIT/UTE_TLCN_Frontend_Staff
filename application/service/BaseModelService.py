from ..service.APIService import APIService

class BaseModelService:
    def __init__(self,url):
        self.url=url
        self.api=APIService()
    def getAll(self):
        return self.api.sendRequest(f'/api/{self.url}/getAll',method='GET')
    def create(self,newModel):
        return self.api.sendRequest(f'/api/{self.url}/create',method='POST',data=newModel)
    def update(self,id,newModel):
        return self.api.sendRequest(f'/api/{self.url}/update/{id}',method='PUT',data=newModel)
    def delete(self,id):
        return self.api.sendRequest(f'/api/{self.url}/delete/{id}',method='DELETE')