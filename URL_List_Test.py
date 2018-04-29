# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 21:43:31 2018

@author: Ben Snell
"""

from URL_List import URL_List

ua = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ' +
        '(KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')
queries = ['social media', 'python']
url_list = URL_List(ua, queries)
the_list = url_list.get_url_list()
for l in the_list:
    print l
