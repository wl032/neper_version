#!/usr/bin/env python2.7
# -*- coding: UTF-8 -*-

import os
import sys
ABSPATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)))
tmpPATH = ABSPATH.split('/')[:-1]
PROPATH = '/'
for path in tmpPATH:
    PROPATH = os.path.join(PROPATH, path)
sys.path.append(PROPATH)

from codes.write_inp_C8 import mysql2inp_C8
from codes.write_inp_C4 import mysql2inp_C4

argv = sys.argv

n = argv.index('-i')
DBName = 'Neper_' + argv[n + 1]
n = argv.index('-o')
INPName = argv[n + 1] + '.inp'

if '--C4' in argv and '--C8' not in argv:
    mysql2inp_C4(INPName, DBName)
elif '--C8' in argv and '--C4' not in argv:
    mysql2inp_C8(INPName, DBName)
else:
    print 'Please choose --C4 or --C8'
