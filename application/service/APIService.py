
import requests
import threading
import datetime
import json
class APIService:
    def __init__(self):
        from ..config import myConfig
        if myConfig.getMODE()=='DEV':
            self.backendURL='http://localhost:5000'
        else:
            pass
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
        from ..config import myConfig
        if method == "GET":
            response=requests.get(self.backendURL + request)
        elif method=='POST':
            response=requests.post(self.backendURL + request, json=data)
        elif method == 'PUT':
            response=requests.put(self.backendURL + request, json=data)
        elif method=='DELETE':
            response=requests.delete(self.backendURL + request)
        print(response)
        myConfig.setIS_WAITING_RESPONSE(False)
        myConfig.setIS_READ_RESPONSE(False)
        return self.convertResponseToJson(response),response.status_code