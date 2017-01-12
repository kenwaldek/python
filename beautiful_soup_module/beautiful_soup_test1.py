#! /usr/bin/env python3
#  -*- coding:utf-8 -*-
###############################################################
# © kenwaldek                         GPL-license
#
# Title: beautiful soup module        Version: 1.0
# Date: 11-1-17                       Language: python3
# Description: beautiful soup web scrapping module examples
#
###############################################################
# do something
import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()

soup = bs.BeautifulSoup(sauce, 'lxml')
# print(soup)

# print(soup.title)
# print(soup.name)
# print(soup.title.string)
# print(soup.find_all('p'))

# for paragraph in soup.find_all('p'):
#     print(paragraph)

# for paragraph in soup.find_all('p'):
#     print(paragraph.text)

# print(soup.get_text)

for url in soup.find_all('a'):
    print(url.get('href'))