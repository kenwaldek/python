#! /usr/bin/env python3
#  -*- coding:utf-8 -*-
###############################################################
# © kenwaldek                         GPL-license
#
# Title: pandas                       Version: 1.0
# Date: 31-12-16                      Language: python3
# Description: panda analyse module voor data
#
###############################################################
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')   #soort style van plot zeggen

web_stats = {"day":[1,2,3,4,5,6],  #dictonary
             "visitors":[43,53,34,45,64,34],
             "bounce_rate":[65,72,62,64,54,66]}

df = pd.DataFrame(web_stats) #df is dataframe

# print(df)
# print(df.set_index('day'))
df.set_index('day', inplace=True)
print(df)
print(df[['visitors','bounce_rate']])
print(df.visitors.tolist())   #uitprinten als een lijst



