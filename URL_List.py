# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 15:39:46 2018

@author: Ben Snell
"""

import urllib2
import urllib
from bs4 import BeautifulSoup
import re

class URL_List:
    
    SEARCH_URL = 'https://www.bing.com/search'
    
    def __init__(self, useragent, queries):
        self.ua = useragent
        self.q = queries
        
    def get_url_list(self, num_results = None):
        headers = {'UserAgent':self.ua}
        url_list = []
        for query in self.q:
            #encode the query
            data = {}
            data['q'] = query
            url_value = urllib.urlencode(data)
            full_url = self.SEARCH_URL + '?' + url_value
            print full_url
            #create the Request object
            request = urllib2.Request(full_url, None, headers)
            #perform the search engine query
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
                #get the html and pass to get_list
                page = response.read()
                url_list.extend(self.__get_list(page))
        return url_list
            
    def __get_list(self, html):
        urls = []
        soup = BeautifulSoup(html, 'html.parser')
        for link in soup.find_all('a'):
            href_data = link.get('href')
            print type(href_data)
            match = re.search('http.*', href_data)
            if match:
                urls.append(match.group(0))
        return urls
        