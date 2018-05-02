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
        
    def get_url_list(self, num_results = 100):
        headers = {'UserAgent':self.ua}
        url_list = []
        for query in self.q:
            query_url_list = []
            url_count = 0
            #encode the query
            data = {}
            data['q'] = query
            url_value = urllib.urlencode(data)
            full_url = self.SEARCH_URL + '?' + url_value
            #create the Request object
            request = urllib2.Request(full_url, None, headers)
            response = self.__open_url(request)
            if response != None:
                #get the html and pass to get_list
                page = response.read()
                url_count = self.__get_results_count(page)
                query_url_list.extend(self.__get_list(page))
            while len(query_url_list) < num_results and len(query_url_list) < url_count:
                data['first'] = len(query_url_list)
                url_value = urllib.urlencode(data)
                full_url = self.SEARCH_URL + '?' + url_value
                #create the Request object
                request = urllib2.Request(full_url, None, headers)
                response = self.__open_url(request)
                if response != None:
                    #get the html and pass to get_list
                    page = response.read()
                    query_url_list.extend(self.__get_list(page))
                else:
                    break
            url_list.extend(query_url_list)
        return url_list
    
    def __open_url(self, request):
        #perform the search engine query
            try:
                response = urllib2.urlopen(request)
            except urllib2.URLError as e:
                if hasattr(e, 'reason'):
                    print 'We failed to reach a server.'
                    print 'Reason: ',e.reason
                    return None
                elif hasattr(e, 'code'):
                    print 'The server could not fulfill the request.'
                    print 'Error code: ',e.code
                    return None
            else:
                return response
            
    def __get_list(self, html):
        urls = []
        soup = BeautifulSoup(html, 'html.parser')
        pattern = re.compile('http.*')
        for link in soup.find_all('a'):
            href_data = link.get('href')
            if type(href_data) is unicode:
                match = pattern.search(href_data)
            else:
                match = None
            if match:
                urls.append(match.group(0))
        return urls
    
    def __get_results_count(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        count_tag = soup.find(class_='sb_count')
        count_str = count_tag.string
        count_str = count_str[:-8]
        count_str = re.sub(',','',count_str)
        count = int(count_str)
        return count