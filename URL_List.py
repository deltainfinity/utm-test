# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 15:39:46 2018

@author: Ben Snell
"""

import urllib2

class URL_List:
    
    def __init__(self, query):
        self.q = query
        
    def get_url_list(self, num_results = None):
                