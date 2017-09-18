# -*- coding: UTF-8 -*-
# Author = k2yk

import threading

def ethread(func,*args,**kwargs):
    t = threading.Thread(target=func,args=args,kwargs=kwargs)
    t.setDaemon(True)
    t.start()

