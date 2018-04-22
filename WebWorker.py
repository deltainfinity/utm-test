# -*- coding: utf-8 -*- 
"""
Created on Wed Apr 18 20:15:24 2018

@author: Ben Snell
"""
import urllib2
import random
from time import sleep

class WebWorker:

    def __init__(self, urls, useragent, alpha):
        self.url_list = urls
        self.user_agent = useragent
        self.a = alpha
        random.seed(None)
    
    def __start_web_requests(self):
        headers = {'User-Agent':self.user_agent}
        for u in self.url_list:
            delay = self.get_delay_time()
            sleep(delay)
            request = urllib2.Request(u, None, headers)
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
    
    def __get_delay_time(self):
        #get a random number between 0 and 1
        random_float = random()
        #get a delta between 0 and the alpha value
        time_delta = random_float * self.ab
        #if the random number is even, increase alpa by delta
        if random_float % 2 == 0:
            alpha = self.a + time_delta
        else: #decrease alpha by delta
            alpha = self.a - time_delta
        #return the calculated delay value
        return alpha
    
