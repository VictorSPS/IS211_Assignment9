#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 9, Assignment 9"""

import urllib2
from bs4 import BeautifulSoup
'''the link provided in Assignment is for April 2015 not January. I used different link to get data for January 2015'''
html = urllib2.urlopen('https://www.wunderground.com/history/airport/KNYC/2015/1/30/MonthlyCalendar.html?req_city=Central%20Park&req_state=NY&req_statename=&reqdb.zip=10106&reqdb.magic=2&reqdb.wmo=99999')
bsObj = BeautifulSoup(html)


def main():
    
    weather = bsObj.findAll('table')
    for w in weather:
        if w.find('a', {"class": "dateText"}) is None:
            pass
        else:
            day = w.find('a', {"class": "dateText"}).get_text()
        if w.find('td', {"class": "value-header"}, text=['Actual:', 'Forecast:']) is None:
            pass
        else:
            temp_type = w.find('td', {"class": "value-header"}, text=['Actual:', 'Forecast:']).get_text()
            if w.find('span', {"class": "high"}) is None:
                pass
            else:
                high_temp = w.find('span', {"class": "high"}).get_text()[:2]
            if w.find('span', {"class": "low"}) is None:
                pass
            else:
                low_temp = w.find('span', {"class": "low"}).get_text()[:2]
            print "Day of Month: {}, Temp Type: {}, High: {}, Low: {}".format(day, temp_type, high_temp, low_temp)

if __name__ == '__main__':
    main()
