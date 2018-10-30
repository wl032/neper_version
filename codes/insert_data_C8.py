#!/usr/bin/env python2.7
# -*- coding: UTF-8 -*-

import MySQLdb
import re


def inp2mqsql_C8(INPname, DBname):

    files = open(INPname)
    lines = files.readlines()
    files.close()

    db = MySQLdb.connect("localhost", "neper", "neper", DBname, charset='utf8')

    cursor = db.cursor()
    state = 0

    for line in lines:
        if line.strip() == '' or line[:5] == '*Part' or line[:4] == '*End':
            continue
        elif line[:5] == '*Node':
            state = 1
        elif line[:8] == '*Element':
            state = 2
        elif line[:6] == '*Elset':
            state = 3
            line = line.replace("\n", "=")
            tmp1 = line.split('=')
            label = tmp1[1]
            sql = "insert into eleset_name(label) values('%s')" % (label)
            try:
                cursor.execute(sql)
                db.commit()
            except BaseException:
                db.rollback()
                print "error3"
        elif line[:5] == '*Nset':
            state = 4
            line = line.replace("\n", "=")
            tmp1 = line.split('=')
            label = tmp1[1]
            sql = "insert into nset_name(label) values('%s')" % (label)
            try:
                cursor.execute(sql)
                db.commit()
            except BaseException:
                db.rollback()
                print "error5"
        elif state == 1:
            tmp1 = line.split(',')
            tmp2 = [eval(item) for item in tmp1]
            [label, x, y, z] = tmp2
            sql = "insert into node(label, x, y, z) \
	    values('%d', '%.8f', '%.8f', '%.8f')" % \
                (label, x, y, z)
            try:
                cursor.execute(sql)
                db.commit()
            except BaseException:
                db.rollback()
                print "error1"
        elif state == 2:
            tmp1 = line.split(',')
            tmp2 = [eval(item) for item in tmp1]
            [label, n1, n2, n3, n4, n5, n6, n7, n8] = tmp2
            sql = "insert into element(label, n1, n2, n3, n4, n5, n6, n7, n8) \
	    values('%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d')" % \
                (label, n1, n2, n3, n4, n5, n6, n7, n8)
            try:
                cursor.execute(sql)
                db.commit()
            except BaseException:
                db.rollback()
                print "error2"
        elif state == 3:
            tmp1 = line.split(',')
            tmp2 = [eval(item) for item in tmp1 if not item.isspace()]
            for e in tmp2:
                sql = "insert into eleset(elset, e) \
	      values('%s', '%d')" % (label, e)
                try:
                    cursor.execute(sql)
                    db.commit()
                except BaseException:
                    db.rollback()
                    print "error4"
        elif state == 4:
            tmp1 = line.split(',')
            tmp2 = [eval(item) for item in tmp1 if not item.isspace()]
            for n in tmp2:
                sql = "insert into nset(nset, n) \
	      values('%s', '%d')" % (label, n)
                try:
                    cursor.execute(sql)
                    db.commit()
                except BaseException:
                    db.rollback()
                    print "error6"

    db.close()


print 'IMPORT insert_data_C8 Success!'
