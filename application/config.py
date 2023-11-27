import datetime 
class Config:
    def __init__(self):
        self.MODE='DEV'
        self.TIMEOUT_REQUEST=1000
        self.DATETIME_REQUEST_CURRENT = None
        self.IS_WAITING_RESPONSE=False
        self.IS_READ_RESPONSE=False
    def getMODE(self):
        return self.MODE
    def getTIMEOUT_REQUEST(self):
        return self.TIMEOUT_REQUEST
    def getDATETIME_REQUEST_CURRENT(self):
        return self.DATETIME_REQUEST_CURRENT
    def getIS_WAITING_RESPONSE(self):
        return self.IS_WAITING_RESPONSE
    def getIS_READ_RESPONSE(self):
        return self.IS_READ_RESPONSE
    def setDATETIME_REQUEST_CURRENT(self,value):
        self.DATETIME_REQUEST_CURRENT=value
    def setIS_WAITING_RESPONSE(self,value):
        self.IS_WAITING_RESPONSE=value
    def setIS_READ_RESPONSE(self,value):
        self.IS_READ_RESPONSE=value
myConfig=Config()
