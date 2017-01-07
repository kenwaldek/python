#! /usr/bin/env python3
#  -*- coding:utf-8 -*-
###############################################################
# © kenwaldek                         GPL-license
#
# Title: quandl module                Version: 1.0
# Date: 05-01-2017                    Language: python3
# Description: working with data and the quandl module
# www.quandl.com
###############################################################
# do something
import quandl
import pandas as pd


df =quandl.get('WIKI/GOOGL') #data via quandl over google
# print(df.head())
df = df[['Adj. Open','Adj. High', 'Adj. Low', 'Adj. Close','Adj. Volume']]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0  # formule High/low %
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0  # formule %

df = df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]
print(df.head())
