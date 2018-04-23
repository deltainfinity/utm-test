# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 15:55:01 2018

@author: Ben Snell
"""
import WebWorker

class URL_Data(WebWorker):
    
    def __init__(self, urls, useragent, alpha):
        super(URL_Data, self).__init__(urls, useragent, alpha)
    
    def get_response(self):
        headers = {'User-Agent':self.user_agent}
        
        