#!/usr/bin/env python2.7
# -*- coding: UTF-8 -*-

import MySQLdb


def element_order_C8(DBname):

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

    sql = "select * from ele_center"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            [e, x, y, z] = row[:-1]
            order = (x * x_colume - 0.5) + \
                (y * y_colume - 0.5) * x_colume + \
                (z * z_colume - 0.5) * y_colume * x_colume + 1
            sql = "update ele_center set ord=%d where e=%d" % (
                round(order), e)
            try:
                cursor.execute(sql)
                db.commit()
            except BaseException:
                db.rollback()
                print "error"
    except BaseException:
        print "Error: unable to fecth data"

    db.close()


print 'IMPORT element_order_C8 Success!'
