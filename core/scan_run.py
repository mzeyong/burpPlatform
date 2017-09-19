# -*- coding: UTF-8 -*-
# Author = k2yk
import imp
import uuid
import os
import time

from lib import easyThread
from lib import send_control

from config import path
from config import scan_control

class run_interface:

    name = ''

    com = {}
    pwd = []
    usr = []
    process = {}
    target = {}
    port = {}
    n_signal = True
    s_signal = True
    p_signal = False

    def start(self,component,ppath=None,upath=None):
        self.init_name(component)
        for ele in range(scan_control.SCAN_LIVE):
            sid = self.init_component(component)
            if sid not in self.com.keys():
                return False
        self.load_pwd(ppath)
        self.load_usr(upath)
        for ele in self.target.keys():
            if self.s_signal:
                while not self.n_signal:
                    time.sleep(0.5)
            sid = self.check_slave_status()
            self.set_target(ele,sid)
            self.set_port(sid)
            self.start_slave(sid)

    def load_pwd(self,ppath=None):
        if ppath:
            pass
        else:
            self.pwd = range(1,20000)

    def load_usr(self,upath=None):
        if upath:
            pass
        else:
            self.usr = [
                'admin',
                'root'
            ]

    def init_name(self,name):
        try:
            self.name = str(name)
        except Exception as error :
            return False

    def init_component(self,component):
        try:
            com = os.listdir(path.COMPONENT)
            for ele in com:
                if ele.endswith('scan.py'):
                    if component in ele:
                        sid = uuid.uuid1()
                        tempImp = imp.load_source(component+'_scan',path.COMPONENT+component+'_scan.py')
                        self.com[sid]=tempImp
                        return sid
        except Exception as error:
            pass

    def set_target(self,target,sid=None):
        try:
            if not sid :
                sid = self.check_slave_status()
                self.com[sid].target = target
            return True
        except Exception as error:
            pass

    def check_slave_status(self):
        try:
            for ele in self.com.keys():
                if self.com[ele].stop_signal :
                    return ele
            return None
        except:
            return None

    def set_port(self,port,sid=None):
        try:
            if not sid :
                sid = self.check_slave_status()
                self.com[sid].port = port
            return True
        except Exception as error:
            pass

    def start_slave(self,sid):
        try:
            if sid in self.com.keys():
                if self.com[sid].stop_signal:
                    pass
                else:
                    send_control.ethread(self.com[sid].scan_thread,self.pwd)
                    self.process[sid] += 1
            else:
                return None
            return None
        except Exception as error:
            return None

    def component_process(self):
        temp = {}
        for ele in self.com.keys():
            temp[ele] = self.com[ele]