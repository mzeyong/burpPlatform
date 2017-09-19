# -*- coding: UTF-8 -*-
# Author = k2yk

import sys

def progress(num):
    rate = float(num) / 100
    rate_num = int(rate * 100)
    r = '\r[%s%s]%d%%' % ("=" * num, " " * (100 - num), rate_num)
    sys.stdout.write(r)
    sys.stdout.flush()

    return