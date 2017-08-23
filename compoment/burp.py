from multiprocessing.dummy import Pool
import Queue
import logging
import time

class burp:
    threat_nums = 10
    thread_pool = None
    result_pool = {}
    empty_flag= False
    target = ''
    port = 0
    user = []
    now_user = ''
    pwd = []
    quest = Queue.Queue()
    argument = {}
    stop_signal = False

    def init_target(self,target,port):
        self.target = target
        self.port = port

    def init_uspw(self,user_list ,password_list):
        self.user = user_list
        self.pwd = password_list

    def init_argument(self,**kwargs):
        self.argument = kwargs

    def start_burp(self):
        '''
        爆破开始信号
        :param uname:
        :param upwd:
        :return:
        '''
        try:
            self.stop_signal = False
            for uele in self.user:
                self.now_user = uele
                self.thread_pool = Pool(processes=self.threat_nums)
                self.thread_pool.map(self.burp_thread,self.pwd)
                self.thread_pool.close()
                self.thread_pool.join()
                logging.info('user '+str(uele)+ ' Done+\n')
            self.stop_signal = True
        except Exception,e:
            logging.error("thread_error :"+ str(e)+"\n")

    def burp_thread(self,password):
        '''
        开始爆破主体，自动多线程执行，毋需手动多线程，
        :param kwargs:
        kwargs 中提供字典集的参数，传输的参数从kwargs中提取
        当前用户获取通过self.now_user 获取，password通过参数自动传入
        避免生成庞大的字典树导致内存爆炸
        结果字典append 到self.result_pool 里面 外部将自动检测是否做完和是否爆破出结果
        :return:
        '''
        if self.stop_signal:
            return None
        try:
            if len(self.argument):
                '''
                获取外部配置属性
                '''
                pass
            '''
            now you burp
            '''
            burp = True
            if burp:
                self.result_pool[self.target+'_'+str(self.port)] = (self.now_user,password)
                self.stop_signal = True
        except Exception,e:
            logging.error(e)

    def checkstate(self):
        while 1:
            if self.stop_signal:
                print (self.result_pool)
                break
            time.sleep(50)




if __name__ == '__main__':
    burpC = burp()
    burpC.init_target('127.0.0.1',3306)
    burpC.init_uspw(['admin1'],['admin1'])
    burpC.start_burp()
    burpC.checkstate()


