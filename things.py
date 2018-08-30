# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 22:42:33 2018

@author: SACHIN
"""

import urllib
import re
from bs4 import BeautifulSoup
import urllib.request  as urllib2 

#data=urllib2.urlopen("https://api.thingspeak.com/update?api_key=VGJG862KVPZ45ZEI&field1=0"+str(900));
#print(data);
data2=urllib2.urlopen("https://api.thingspeak.com/channels/454132/feeds.json?api_key=B5RAKEI89R6VS760&results=2")
select = repr(data2.read(['field1']))
#select=select[300:]

#pick=re.search('field1":"(.+?)",',select)
if pick:
    print(pick.group())