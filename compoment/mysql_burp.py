# -*- coding: UTF-8 -*-
import MySQLdb
import burp
import logging

class mysql_burp(burp.burp):
    def burp_thread(self,password):
        if self.stop_signal:
            return None
        try:
            db = MySQLdb.connect(host=self.target,port=self.port,user=self.now_user,passwd=password)
            db.close()
            self.result_pool[self.target+'_'+str(self.port)] = (self.now_user,password)
            self.stop_signal = True
        except Exception,e:
            logging.error(e)

if __name__ == '__main__':
    burp_test = mysql_burp()
    burp_test.init_target('127.0.0.1',3306)
    burp_test.init_uspw(['root'],['root'])
    burp_test.start_burp()
    burp_test.checkstate()
