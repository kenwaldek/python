#! /usr/bin/env python3
#  -*- coding:utf-8 -*-
###############################################################
# © kenwaldek                         GPL-license
#
# Title: beautiful soup module        Version: 1.0
# Date: 11-1-17                       Language: python3
# Description: beautiful soup navigating tags
#
###############################################################
# do something
import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()

soup = bs.BeautifulSoup(sauce, 'lxml')

nav = soup.nav
# print(nav)
for url in nav.find_all('a'):
    print(url.get('href'))

body = soup.body
for paragraph in body.find_all('p'):
    print(paragraph.text)

