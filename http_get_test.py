# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 20:15:24 2018

@author: Ben Snell
"""
import urllib2

url='http://www.google.com'
user_agent = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
    '(KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')
headers = {'User-Agent':user_agent}
request = urllib2.Request(url,None,headers)
try:
    response = urllib2.urlopen(request)
except urllib2.URLError as e:
    if hasattr(e, 'reason'):
        print 'We failed to reach a server.'
        print 'Reason: ',e.reason
    elif hasattr(e, 'code'):
        print 'The server could not fulfill the request.'
        print 'Error code: ',e.code
else:
    print 'Success'

page = response.read()
#print page

