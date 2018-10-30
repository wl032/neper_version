#!/usr/bin/env python2.7
# -*- coding: UTF-8 -*-

import os, sys
from optparse import OptionParser

ABSPATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)))
tmpPATH = ABSPATH.split('/')[:-1]
PROPATH = '/'
for path in tmpPATH:
    PROPATH = os.path.join(PROPATH, path)
sys.path.append(PROPATH)

from codes.element_center_C8 import element_center_C8
from codes.element_order_C8 import element_order_C8
from codes.write_damask_C8 import write_damask

optParser = OptionParser()

optParser.add_option('-i','--input',action = 'store',type = "string" ,dest = 'DBName')
optParser.add_option('-o','--output',action = 'store',type = "string" ,dest = 'GEOMName')

option , args = optParser.parse_args()

DBName = 'Neper_' + option.DBName
GEOMName = option.GEOMName + '.geom'

element_center_C8(DBName)
element_order_C8(DBName)
write_damask(DBName, GEOMName)


