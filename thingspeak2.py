# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 04:42:07 2018

@author: SACHIN
"""

import urllib.request  as urllib2 
import json
import time
temp=[]
ph=[]
dept=[]
flow=[]
lid=[]
naler=[]
TS = urllib2.urlopen("https://api.thingspeak.com/channels/463629/feeds.json?results=406")

response = TS.read()
data=json.loads(response)

a = data['feeds']
for i in range(0,len(a)):
    b = a[i]
    c = b['field1']
    temp.append(c)
 


for i in range(0,len(a)):
    b = a[i]
    c = b['field2']
    ph.append(c)
  


for i in range(0,len(a)):
    b = a[i]
    c = b['field3']
    dept.append(c)



for i in range(0,len(a)):
    b = a[i]
    c = b['field4']
    flow.append(c)
  
  


for i in range(0,len(a)):
    b = a[i]
    c = b['field6']
    lid.append(c)



for i in range(0,len(a)):
    b = a[i]
    c = b['field7']
    naler.append(c)



time.sleep(5)
print(temp)
print(ph)
print(dept)
print(flow)
print(lid)
print(naler)
TS.close()