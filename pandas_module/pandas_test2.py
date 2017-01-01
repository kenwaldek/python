#! /usr/bin/env python3
#  -*- coding:utf-8 -*-
###############################################################
# © kenwaldek                         GPL-license
#
# Title: pandas                       Version: 1.0
# Date: 31-12-16                      Language: python3
# Description: import csv file with panda
#
###############################################################
import pandas as pd
df = pd.read_csv('test.csv')

# print(df.head())  #print de eerste regels van csvv file tail de laatste
df.set_index('Date', inplace=True)

df.to_csv('newtest.csv') # data uitprinten naar csv file

df = pd.read_csv('newtest.csv')  #terug inlezen
print(df.head())  #spring head uit eerste regels dus

df = pd.read_csv('newtest.csv', index_col=0)  #terug inlezen en eerste rij als index plaatsen rij'0"
print(df.head())





