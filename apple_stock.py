#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Week 9, Assignment 9"""
    
import urllib2
from bs4 import BeautifulSoup
html = urllib2.urlopen('https://finance.yahoo.com/quote/AAPL/history?p=AAPL')
bsObj = BeautifulSoup(html)

stock_data = bsObj.findAll('tr')

def main():
    """Parses table rows from given URL and returns date and closing price of stock"""
    print "Apple Inc. (AAPL) Daily Closing Prices:"
    for i in stock_data:
        t_data = i.findAll('td')
        if len(t_data) is 7:
            date = t_data[0].contents[0]
            close = t_data[4].contents[0]
            print ("Date: {}, Closing Price: {}").format(date, close)

if __name__ == '__main__':
    main()
