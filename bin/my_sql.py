#!/usr/bin/env python2.7
# -*- coding: UTF-8 -*-

import MySQLdb
import sys

argv = sys.argv

if '--show' in argv:
	db = MySQLdb.connect("localhost", "neper", "neper", charset='utf8' )
	cursor = db.cursor()
	sql = "show databases"
	cursor.execute(sql)
	results = cursor.fetchall()
	print '-*-*-*-*-*-*-*-'
	for row in results[1:]:
		print row[0][6:]
	print '-*-*-*-*-*-*-*-'
	db.close()
elif '--add' in argv:
	db = MySQLdb.connect("localhost", "root", "root", charset='utf8' )
	cursor = db.cursor()
	n = argv.index('--add')
	DBName = argv[n+1]
	sql = "create database %s" %('Neper_' + DBName)
	cursor.execute(sql)
	sql = "grant all privileges on %s.* to 'neper'@'localhost' identified by 'neper'" \
	 %('Neper_' + DBName)
	cursor.execute(sql)
	db.close()
elif '--del' in argv:
	db = MySQLdb.connect("localhost", "neper", "neper", charset='utf8' )
	cursor = db.cursor()
	n = argv.index('--del')
	DBName = argv[n+1]
	sql = "drop database %s" %('Neper_' + DBName)
	cursor.execute(sql)
	db.close()
else:
	print 'Please choose --show or --add or --del'
	