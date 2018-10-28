#!/usr/bin/env python2.7
# -*- coding: UTF-8 -*-

import MySQLdb
import math

def mysql2inp_C4(INPname, DBname):

	files = open(INPname,'w')
	
	db = MySQLdb.connect("localhost", "neper", "neper", DBname, charset='utf8' )
	cursor = db.cursor()
	
	files.write('*Node\n')
	
	sql = "select * from node"
	try:
	  cursor.execute(sql)
	  results = cursor.fetchall()
	  for row in results:
	    [label, x, y, z] = row
	    files.write(str('%d, %.8f, %.8f, %.8f'%(label, x, y, z))+'\n')
	except:
	  print "Error: unable to fecth data"
	
	files.write('*Element, type=C3D4\n')
	
	sql = "select * from element"
	try:
	  cursor.execute(sql)
	  results = cursor.fetchall()
	  for row in results:
	    [label, n1, n2, n3, n4] = row
	    files.write(str('%d, %d, %d, %d, %d'\
			    %(label, n1, n2, n3, n4))+'\n')
	except:
	  print "Error: unable to fecth data"
	  
	sql = "select * from eleset_name"
	try:
	  cursor.execute(sql)
	  results = cursor.fetchall()
	  for row in results:
	    label = row[0]
	    sql = "select count(*) from eleset where elset='%s'"%label
	    try:
	      cursor.execute(sql)
	      count = cursor.fetchall()[0][0]
	      n = int(math.ceil(count/8.0))
	      files.write(str('*Elset, elset=%s'%label)+'\n')
	      for i in range(n):
				sql = "select * from eleset where elset='%s' limit %d,8"\
				  %(label,8*i)
				try:
				  cursor.execute(sql)
				  results1 = cursor.fetchall()
				  for e in results1:
				    files.write(str('%d, '%e[1]))
				except:
				  print "Error: unable to fecth data"
				files.write('\n')
	    except:
	      print "Error: unable to fecth data"
	except:
	  print "Error: unable to fecth data"
	
	sql = "select * from nset_name"
	try:
	  cursor.execute(sql)
	  results = cursor.fetchall()
	  for row in results:
	    label = row[0]
	    sql = "select count(*) from nset where nset='%s'"%label
	    try:
	      cursor.execute(sql)
	      count = cursor.fetchall()[0][0]
	      n = int(math.ceil(count/8.0))
	      files.write(str('*Nset, nset=%s'%label)+'\n')
	      for i in range(n):
				sql = "select * from nset where nset='%s' limit %d,8"\
				  %(label,8*i)
				try:
				  cursor.execute(sql)
				  results1 = cursor.fetchall()
				  for nd in results1:
				    files.write(str('%d, '%nd[1]))
				except:
				  print "Error: unable to fecth data"
				files.write('\n')
	    except:
	      print "Error: unable to fecth data"
	except:
	  print "Error: unable to fecth data"
	
	db.close()
	files.close()


print 'IMPORT write_inp_C4 Success!'