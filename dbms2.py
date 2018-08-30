# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 05:20:18 2018

@author: SACHIN
"""

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","","test" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.

data = cursor.fetchone()
print ("Database version : %s " % data)

# disconnect from server
db.close()