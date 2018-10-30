#!/usr/bin/env python2.7
# -*- coding: UTF-8 -*-

import MySQLdb
import re


def indices_as_order(DBname):

    db = MySQLdb.connect("localhost", "neper", "neper", DBname, charset='utf8')

    cursor = db.cursor()

    cursor.execute("drop table if exists damask_indice")
    db.commit()

    sql = "create table damask_indice(i int)"
    cursor.execute(sql)
    db.commit()

    sql = "select e from ele_center order by ord"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            e = row[0]
            sql = "select elset from eleset where e=%d" % e
            try:
                cursor.execute(sql)
                indice = cursor.fetchone()[0]
                indice = int(re.findall(r"\d+", indice)[0])
                sql = "insert into damask_indice(i) values('%d')" % indice
                try:
                    cursor.execute(sql)
                    db.commit()
                except BaseException:
                    db.rollback()
                    print "error"
            except BaseException:
                print "Error: unable to fecth data"
    except BaseException:
        print "Error: unable to fecth data"

    db.close()


def write_damask(DBname, GEOMname):

    indices_as_order(DBname)

    files = open(GEOMname, 'w')

    db = MySQLdb.connect("localhost", "neper", "neper", DBname, charset='utf8')

    cursor = db.cursor()

    sql = "select count(*) from node"
    cursor.execute(sql)
    n_total = cursor.fetchone()[0]

    sql = "select count(*) from nset where nset='x0'"
    cursor.execute(sql)
    x_colume = n_total / cursor.fetchone()[0] - 1

    sql = "select count(*) from nset where nset='y0'"
    cursor.execute(sql)
    y_colume = n_total / cursor.fetchone()[0] - 1

    sql = "select count(*) from nset where nset='z0'"
    cursor.execute(sql)
    z_colume = n_total / cursor.fetchone()[0] - 1

    sql = "select * from damask_indice"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        state = 0
        for row in results:
            i = row[0]
            files.write(str('%d ' % i))
            state = state + 1
            if state == x_colume:
                files.write('\n')
                state = 0
    except BaseException:
        print "Error: unable to fecth data"

    db.close()

print 'IMPORT write_damask_C8 Success!'
