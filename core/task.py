# -*- coding: UTF-8 -*-
# Author = k2yk

import time
from core import burp_run
from core import scan_run



class task:
    b_interface = burp_run.run_interface
    s_interface = scan_run.run_interface
    load_signal = False
    end_signal = False
    component = []
    live_com = []

    def get_total_process(self):
        pass

    def get_scan_process(self):
        pass

    def get_component_process(self,component):
        pass

    def init_target(self):
        pass

    def start(self):
        pass

    def task_check(self):
        while True:
            if self.load_signal:
                time.sleep(0.5)
                message = 'loading config ...'
                print message
                continue
            for ele in self.component:
                # status = self.getProcess(ele)
                status = self.get_total_process()
                if status == 1:
                    message =  str(ele)+' finish'
                elif status == 0:
                    message = str(ele) + ' finish'
                else:
                    message = str(ele) + ' process status:' + str(status)
                # print str(ele) + ' process status:' + str(total)
                print message

                time.sleep(1)
                if self.end_signal :
                    if '/' in status:
                        now,total = status.split('/')
                        if int(now) == int(total):
                            message = 'all task finish'
                            print message
                            return True