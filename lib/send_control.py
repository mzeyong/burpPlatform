# coding=utf-8

from config import send_control
import time
from lib.easyThread import ethread

class sendControl:
    @staticmethod
    def scan_control(runFunc,valList):
        cou = 0
        for ele in valList:
            ethread(func=runFunc,args=(ele,))
            time.sleep(send_control.SCAN)
            if cou % 100 == 0:
                time.sleep(send_control.SAFE_TIME)
                cou = 0
            cou += 1


    @staticmethod
    def burp_control(runFunc,runDict):
        cou = 0
        for ele in runDict:
            ethread(func=runFunc,args=(ele,))
            time.sleep(send_control.BURP)
            if cou % 100 == 0:
                time.sleep(send_control.SAFE_TIME)
                cou = 0

