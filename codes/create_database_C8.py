#!/usr/bin/env python2.7
# -*- coding: UTF-8 -*-

import MySQLdb


def create_DB_C8(DBname):

    db = MySQLdb.connect("localhost", "neper", "neper", DBname, charset='utf8')

    cursor = db.cursor()

    cursor.execute("drop table if exists nset")
    cursor.execute("drop table if exists nset_name")
    cursor.execute("drop table if exists eleset")
    cursor.execute("drop table if exists eleset_name")
    cursor.execute("drop table if exists element")
    cursor.execute("drop table if exists node")

    sql = """create table node(
	  label int primary key,
	  x double,
	  y double,
	  z double)"""
    cursor.execute(sql)

    sql = """create table element(
	  label int primary key,
	  n1 int,
	  n2 int,
	  n3 int,
	  n4 int,
	  n5 int,
	  n6 int,
	  n7 int,
	  n8 int,
	  constraint fk_n1 foreign key(n1) references node(label),
	  constraint fk_n2 foreign key(n2) references node(label),
	  constraint fk_n3 foreign key(n3) references node(label),
	  constraint fk_n4 foreign key(n4) references node(label),
	  constraint fk_n5 foreign key(n5) references node(label),
	  constraint fk_n6 foreign key(n6) references node(label),
	  constraint fk_n7 foreign key(n7) references node(label),
	  constraint fk_n8 foreign key(n8) references node(label))"""
    cursor.execute(sql)

    sql = """create table eleset_name(
	  label char(10) primary key)"""
    cursor.execute(sql)

    sql = """create table eleset(
	  elset char(10),
	  e int,
	  constraint fk_elset foreign key(elset) references eleset_name(label),
	  constraint fk_e foreign key(e) references element(label))"""
    cursor.execute(sql)

    sql = """create table nset_name(
	  label char(10) primary key)"""
    cursor.execute(sql)

    sql = """create table nset(
	  nset char(10),
	  n int,
	  constraint fk_nset foreign key(nset) references nset_name(label),
	  constraint fk_n foreign key(n) references node(label))"""
    cursor.execute(sql)
    db.commit()

    db.close()


print 'IMPORT create_database_C8 Success!'
