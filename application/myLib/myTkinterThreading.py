from tkinter import messagebox
from threading import *
import time
import datetime

class MyTkinterThreading:
    def __init__(self):
        pass
    def startWaiting(self,message,labelObject,functionCheckStatus):
        self.threadWaiting=Thread(target=self.waiting,args=(message,labelObject,functionCheckStatus))
        self.threadWaiting.start()
    def waiting(self,message,labelObject,functionCheckStatus):
        current_datetime = datetime.datetime.now()
        self.isWaiting = True
        wait=True
        while wait:
            labelObject.config(text=message+'.'*((datetime.datetime.now()-current_datetime).seconds%3+1))
            time.sleep(0.25)
            wait=functionCheckStatus()
        labelObject.config(text="")
    def newThread(self,function,arguments=(),labelObject=None,message="Hệ thống đang xử lý ",functionCheckStatus=None,functionSetCheck=None):
        if labelObject is not None:
            functionSetCheck(False)
            time.sleep(0.25)
            functionSetCheck(True)
            self.startWaiting(message,labelObject,functionCheckStatus)
        t=Thread(target=function,args=arguments)

        t.start()