#!/usr/bin/env python2.7
# -*- coding: UTF-8 -*-

import MySQLdb


def element_center_C8(DBname):

    db = MySQLdb.connect("localhost", "neper", "neper", DBname, charset='utf8')

    cursor = db.cursor()

    cursor.execute("drop table if exists node_link")
    cursor.execute("drop table if exists ele_center")
    db.commit()

    sql = """create table node_link(
    n int,
    e int,
    constraint fk_n_link foreign key(n) references node(label),
    constraint fk_e_link foreign key(e) references element(label))"""
    cursor.execute(sql)

    sql = """create table ele_center(
    e int,
    x double,
    y double,
    z double,
    ord int,
    constraint fk_e_center foreign key(e) references element(label))"""
    cursor.execute(sql)

    db.commit()

    sql = "select * from element"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            e = row[0]
            sql = "insert into ele_center(e, x, y, z, ord) values('%d', '%.8f', '%.8f', '%.8f', '%d')" % (
                e, 0.0, 0.0, 0.0, 0)
            try:
                cursor.execute(sql)
                db.commit()
            except BaseException:
                db.rollback()
                print "error"
            for n in row[1:]:
                sql = "insert into node_link(n, e) values('%d', '%d')" % (n, e)
                try:
                    cursor.execute(sql)
                    db.commit()
                except BaseException:
                    db.rollback()
                    print "error"
    except BaseException:
        print "Error: unable to fecth data"

    sql = "select * from node"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            [label, x, y, z] = row
            sql = "select * from node_link where n=%d" % label
            try:
                cursor.execute(sql)
                results1 = cursor.fetchall()
                for e in results1:
                    sql = "update ele_center set x=x+%.8f,y=y+%.8f,z=z+%.8f where e=%d" \
                        % (x / 8, y / 8, z / 8, e[1])
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


print 'IMPORT element_center_C8 Success!'
