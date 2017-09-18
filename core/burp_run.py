# -*- coding: UTF-8 -*-
# Author = k2yk
import imp
import uuid
import os
from lib import easyThread
from lib import send_control


class run_interface:

    name = ''

    com = {}
    pwd = []
    usr = []

    def start(self):
        pass

    def init_name(self,name):
        try:
            self.name = str(name)
        except Exception as error :
            return False

    def init_component(self,component):
        try:
            os.path.isdir
        except Exception as error:
            pass

    def set_target(self,target):
        try:
            free_slave = self.check_slave_status()
            if free_slave:
                self.com[free_slave].target = target
                return True
            else:
                return False
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

    def set_port(self,port):
        try:
            free_slave = self.check_slave_status()
            if free_slave:
                self.com[free_slave].port = port
                return True
            else:
                return False
        except Exception as error:
            pass


    def pd(self):
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