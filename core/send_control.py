# coding=utf-8

from config import send_control
import time
from lib.easyThread import ethread

class sendControl:
    @staticmethod
    def scan_control(runFunc,valList):
        for ele in valList:
            time.sleep(send_control.SCAN)
            ethread(func=runFunc,args=(ele,))

    @staticmethod
    def burp_control(runFunc,runDict):
        for ele in runDict:
            time.sleep(send_control.BURP)
            ethread(func=runFunc,args=(ele,))
