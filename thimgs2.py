# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 04:14:08 2018

@author: SACHIN
"""

import json
import urllib.request  as urllib2 
def main():
    conn = urllib2.urlopen("https://api.thingspeak.com/channels/454132/feeds.json?api_key=B5RAKEI89R6VS760&results=2")

    response = conn.read()
    print ("http status code=%s")
    data=json.loads(response)
    print (data['field1'])
    conn.close()

if __name__ == '__main__':
    main()