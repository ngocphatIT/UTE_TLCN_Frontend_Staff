
import requests
from tkinter import messagebox
import json
from ..service.SQLLiteService import SessionDataService
_session = SessionDataService
#{'Authorization':'eyJhbGciOiAiU0hBMjU2IiwgInR5cCI6ICJKV1QifQ==.eyJleHAiOiAiMjAyMy0xMi0wOCAwMToxMDoxOCIsICJpYXQiOiAiMjAyMy0xMi0wNyAxMzoxMDoxOCIsICJzdWIiOiA5OTkyNDg1MjksICJyb2xlIjogIkFETUlOIiwgIm9iamVjdCI6IHt9fQ==.81456ee50f0aa12e0d29bd9335c2f4d917fdbf47d4a04cc3905cd2551707c0f5'}
class APIService:
    def __init__(self):
        # from ..config import myConfig
        # if myConfig.getMODE()=='DEV':
            self.backendURL='http://backendtlcn.devforfuture.com/'
            # self.backendURL='http://127.0.0.1:5000/'
        # else:
            # pass
    # def sendRequest(self, request, data={}, method="GET"):
    #     from ..config import myConfig
    #     isCanSendRequest = False
        
    #     if myConfig.getDATETIME_REQUEST_CURRENT() is None:
    #         isCanSendRequest=True
    #     else:
    #         if datetime.datetime.now().timestamp()*1000-myConfig.getDATETIME_REQUEST_CURRENT().timestamp()*1000>=1:
    #             if not myConfig.getIS_WAITING_RESPONSE():
    #                 isCanSendRequest=True
    #     myConfig.setDATETIME_REQUEST_CURRENT( datetime.datetime.now())
    #     if isCanSendRequest:
    #         print('Da gui')
    #         myConfig.setIS_WAITING_RESPONSE(True)
    #         t=threading.Thread(target=self.sendRequestAction, args=(request,data,method))
    #         t.start()
    def convertResponseToJson(self,response):
        my_json = response.content.decode('utf8')
        return json.loads(my_json)
    def sendRequest(self, request, data={}, method="GET"):
        headers={'Authorization':_session().getAuthorization()}
        try:
            if method == "GET":
                response=requests.get(self.backendURL + request,headers=headers)
            elif method=='POST':
                response=requests.post(self.backendURL + request, json=data,headers=headers)
            elif method == 'PUT':
                response=requests.put(self.backendURL + request, json=data,headers=headers)
            elif method=='DELETE':
                response=requests.delete(self.backendURL + request,headers=headers)
            return {'message':self.convertResponseToJson(response),'status_code':response.status_code}
        except Exception as e:
            print(e)
            if 'ConnectionError' in str(e):
                messagebox.showerror('Lỗi kết nối','Mất kết nối với server')
    def logout(self):
        try:
            headers={'Authorization':_session().getAuthorization()}
            response=requests.get(self.backendURL + '/api/auth/logout/'+_session().getAuthorization(),headers=headers)
            return {'message':'','status_code':response.status_code}
        except Exception as e:
            print(e)
            if 'ConnectionError' in str(e):
                messagebox.showerror('Lỗi kết nối','Mất kết nối với server')

