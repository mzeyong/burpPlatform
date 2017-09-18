# -*- coding: UTF-8 -*-
# Author = k2yk
import imp
import uuid
import os

from lib import easyThread
from lib import send_control

from config import path
from config import burp_control

class run_interface:

    name = ''

    com = {}
    pwd = []
    usr = []
    target = {}
    port = {}
    n_signal = True

    def start(self,component):
        self.init_name(component)
        for ele in range(burp_control.BURP_LIVE):
            sid = self.init_component(component)
            if sid not in self.com.keys():
                return False
        for ele in self.target.keys():
            while self.n_signal:
                sid = self.check_slave_status()
                self.set_target(ele,sid)
                self.set_port(sid)
                self.start_slave(sid)

    def load_pwd(self,ppath):
        pass

    def load_usr(self,upath):
        pass

    def init_name(self,name):
        try:
            self.name = str(name)
        except Exception as error :
            return False

    def init_component(self,component):
        try:
            com = os.listdir(path.COMPONENT)
            for ele in com:
                if ele.endswith('burp.py'):
                    if component in ele:
                        sid = uuid.uuid1()
                        tempImp = imp.load_source(component+'_burp',path.COMPONENT+component+'_burp.py')
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
                send_control.ethread(self.com[sid].burp_thread,self.pwd)
            else:
                return None
            return None
        except Exception as error:
            return None

    def component_process(self):
        pass