#!bin/bash/python

import requests
import bs4
from bs4 import BeautifulSoup

URL = 'http://www.gallup.com/poll/201617/gallup-daily-trump-job-approval.aspx'
site = requests.get(URL)
soup = BeautifulSoup(site.text,'html.parser')# , from_encoding="utf-8")

'''First build it as a scraper, then convert to class'''
# class Gallup_scraper(self,URL):
#     '''This scraper pulls information from Gallup websites.'''
#     URL = self.URL
#     result =
#     def extract_dates(self):
#         '''Pull out the dates from the graph you are looking at.'''
#         target = results.find_all

def extract_dates(soup):
    dates = soup.find_all(name ='p',attrs={'class':'dv_tooltip_value'})
    datelist = []
    for d in dates:
        datelist.append(d.text)
    return datelist

def extract_lines(soup):
    lines = soup.find_all(name='p',attrs={'dv-data-line'})
    data = {}
    for line in lines:
        label =  soup.find(name = 'span',attrs={'class':'dv-tooltip-line-label'}).text
        dataset = soup.find_all(name='span', attrs={'class': 'dv-tooltip-value'})
        datanums = [d.text for d in dataset]
        data[label]=datanums
    return data

print extract_dates(soup)
print extract_lines(soup)
