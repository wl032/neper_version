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

from codes.insert_data_C8 import inp2mqsql_C8
from codes.create_database_C8 import create_DB_C8
from codes.insert_data_C4 import inp2mqsql_C4
from codes.create_database_C4 import create_DB_C4

argv = sys.argv

n = argv.index('-i')
INPName = argv[n + 1] + '.inp'
n = argv.index('-o')
DBName = 'Neper_' + argv[n + 1]

if '--C4' in argv and '--C8' not in argv:
    create_DB_C4(DBName)
    inp2mqsql_C4(INPName, DBName)
elif '--C8' in argv and '--C4' not in argv:
    create_DB_C8(DBName)
    inp2mqsql_C8(INPName, DBName)
else:
    print 'Please choose --C4 or --C8'
