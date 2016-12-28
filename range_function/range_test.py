#! /usr/bin/env python3
#  -*- coding:utf-8 -*-
###############################################################
# © kenwaldek
#
# Title: range function                   Version: 1.0
# Date: 28-12-16                          Language: python3
# Description: de range funktie uitgelegd
#
###############################################################

# range word een generator genoemd
for i in range (10):  #print 10x do something
    #do something
    print('hello  world') #  hetgeen uitgevoerd zal worden

print('#########')

xyz = [i for i in range (10)] #vierkante haakjes wordt in memory geladen
print('done')
xyz = (i for i in range (10)) #dit is  een "generator object"
print(xyz)

#todo zoek meer info over "generator objects"