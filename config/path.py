# -*- coding: UTF-8 -*-
# Author = k2yk

import os

SP = '\\\\' if 'NT' in os.name else '/'

COMPONENT = os.getcwd()+ SP + 'component' +SP

DATAPATH = os.getcwd()+ SP + 'data' +SP