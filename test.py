#!/usr/bin/python
import mysql.connector
from mysql.connector import errorcode
import sys, os, csv, re

config = {
  'user': 'fabric',
  'password': 'Fabpass1!',
  'host': '10.200.7.188',
  'database': 'SERWIS20',
  'raise_on_warnings': True,
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()
duble = ("SELECT COUNT(*) - COUNT(DISTINCT SN) AS SN  FROM service")

cursor.execute(duble)
row = cursor.fetchall()
for j in row:
    print(row[0])

query = ("INSERT INTO service "
               "(`SN`,`status`,`problem_element`,`uid_in`, `stage_from`)"
               "VALUES ('005D01098999','1','no','666','6000')")
dublea = ("SELECT COUNT(*) - COUNT(DISTINCT SN) AS SN  FROM service")

cursor.execute(query)
cursor.execute(dublea)
rowa= cursor.fetchall()
for i in rowa:
    print(rowa[0])
if j == i:
    print("NOT duble")
else:
    print("Yes")
     
cursor.close()
cnx.close()
 
 
 
 
 
 
 
 
 
 


