from ..service.APIService import APIService
class AuthenticationService:
    def __init__(self):
        pass
    def login(self, username, password):
        return APIService().sendRequest(request='/api/auth/login',data={'username':username,'password': password,'role':'admin'},method='POST')
    def changePassword(self,username,oldPassword,newPassword):
        return APIService().sendRequest(request='/api/auth/changePassword',data={'username':username,'oldPasswordHash':oldPassword,'newPasswordHash':newPassword},method='POST')
