#! /usr/bin/env python3
#  -*- coding:utf-8 -*-
###############################################################
# © kenwaldek                             GPL-license
#
# Title: zip functie                      Version: 1.0
# Date: 28-12-16                          Language: python3
# Description: zip is het bij elkaar voegen van variablen
#
###############################################################
#  more info https://docs.python.org/3/library/functions.html#zip

x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
z = ['a', 'b', 'c']
### onderstaande print lijst van a en b
for a, b, c in zip(x, y, z):  # abc zijn tijdelijke variabelen
    print(a, b)
### onderstaande geeft tupples weer van de lijsten
print(zip(x, y, z))

for i in zip(x, y, z):
    print(i) # worden weergegeven als tupples



