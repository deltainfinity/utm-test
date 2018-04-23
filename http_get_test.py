# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 20:49:16 2018

@author: Ben Snell
"""

from WebWorker import WebWorker

urls = ['http://www.google.com','http://www.facebook.com','https://www.siqute.com']
ua = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ' +
        '(KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')
worker = WebWorker(urls, ua, 2.0)
results = worker.start_web_requests()
for r in results:
    print "Retrieved " + r + " in " + str(results[r]) + " seconds."
    

