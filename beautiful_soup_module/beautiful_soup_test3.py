#! /usr/bin/env python3
#  -*- coding:utf-8 -*-
###############################################################
# © kenwaldek                         GPL-license
#
# Title: beautiful soup module        Version: 1.0
# Date: 11-1-17                       Language: python3
# Description: beautiful soup and tables
#
###############################################################
# do something
import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()

soup = bs.BeautifulSoup(sauce, 'lxml')

# table = soup.table
# print(table)

table = soup.find('table')
table_row = table.find_all('tr')
for tr in table_row:
    td = tr.find_all('td')
    row = [i.text for i in td]
    print(row)

## pandas module is een betere manier om tables te vinden en berekeningen mee te doen